#!/usr/bin/python
import os
from conans.client.conan_api import Conan
from conans.errors import ConanException
from pathlib import Path
from eprint import eprint
import json
from copy import copy

conan_command_line, _, _ = Conan.factory()


class Signature:
    def __init__(self):
        self.version = ""
        self.channel = ""
        self.user = ""

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, val):
        self.__version = val

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, val):
        self.__channel = val

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, val):
        self.__user = val


class BuilderConfig:
    def __init__(self):
        self.host_profile = None
        self.build_profile = None
        self.host_settings = ""
        self.excludes = []
        self.includes = []

    @property
    def host_profile(self):
        return self.__host_profile

    @host_profile.setter
    def host_profile(self, val):
        self.__host_profile = val

    @property
    def build_profile(self):
        return self.__build_profile

    @build_profile.setter
    def build_profile(self, val):
        self.__build_profile = val

    @property
    def host_settings(self):
        return self.__host_settings

    @host_settings.setter
    def host_settings(self, val):
        self.__host_settings = val

    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, val):
        self.__excludes = val


class ConanPackage:
    def __init__(self, signature=Signature(), path='.'):
        if ".py" not in path:
            path = f'{path}/conanfile.py'
        self.name = ""
        self._signature = copy(signature)
        self._read_package_attributes(path)
        self.path = str(path).replace("conanfile.py", "")

    def get_path(self):
        return self.path

    def get_pattern(self):
        return f"{self.name}/{self._signature.version}@{self._signature.user}/{self._signature.channel}"

    def _get_attribute(self, path , attribute, fail_on_invalid=False):
        attribute = str(attribute)
        try:
            conan_package = conan_command_line.inspect(path=f'{path}', attributes=[f'{attribute}'])
            return conan_package.get(attribute)
        except ConanException:
            if fail_on_invalid:
                raise Exception(f"Attribute not found: {attribute} in {path} - {ConanException}")
        return ""

    def _read_package_attributes(self, path):
        conan_package = conan_command_line.inspect(path=f'{path}', attributes=["name"])
        self.name = self._get_attribute(path,'name', True)
        version = self._get_attribute(path,'version')
        if version != "":
            self._signature.version = version
        user = self._get_attribute(path,'user')
        if user != "":
            self._signature.user = user
        channel = self._get_attribute(path,'channel')
        if channel != "":
            self._signature.channel=channel

    def _check_includes(self, includes):
        if len(includes) > 0:
            for include in includes:
                if include in self.path:
                    return True
            return False
        return True

    def is_withing_scope(self, configuration=BuilderConfig()):
        if not self._check_includes(configuration.includes):
            return False
        for exclude in configuration.excludes:
            if exclude in self.path:
                return False
        return True

    def export(self):
        conan_command_line.export(self.path,
                                  self.name,
                                  self._signature.version,
                                  self._signature.user,
                                  self._signature.channel)

    def create(self, configuration=BuilderConfig()):
        conan_command_line.create(self.path,
                                  name=self.name,
                                  version=self._signature.version,
                                  user=self._signature.user,
                                  channel=self._signature.channel,
                                  profile_names=configuration.host_profile,
                                  profile_build=configuration.build_profile,
                                  settings=configuration.host_settings,
                                  test_build_folder=f'/tmp/{self.pattern}/tbf')
    def source(self)
        conan_command_line.source(self.path,
                                 source_folder=f"{self.path}/tmp")

    def get_build_order(self, configuration=BuilderConfig()):
        installfolder = "/home/michel/projects/DisroopConanPackages/build"
        print(configuration.host_profile)
        # conan_command_line.install(path=self.path,
        #                             name=self.name, 
        #                             version=self._signature.version,
        #                             user=self._signature.user,
        #                             channel=self._signature.channel,
        #                             profile_names=configuration.host_profile,
        #                             profile_build=configuration.build_profile,
        #                             settings=configuration.host_settings,
        #                             install_folder= installfolder)
        pattern = self.get_pattern()
        conan_command_line.remove_locks()
        conan_command_line.lock_create(path=None,
            lockfile_out="app.lock",
        reference=pattern,
                                        profile_host=configuration.host_profile,
                                        profile_build=configuration.build_profile,
                                        build="missing")

        #                             version=self._signature.version,
        #                             user=self._signature.user,
        #                             channel=self._signature.channel,
        #                             profile_names=configuration.host_profile,
        #                             profile_build=configuration.build_profile,
        #                             settings=configuration.host_settings,
        #                             install_folder= installfolder
        #conan_command_line.info_build_order(reference=self.get_pattern(), 
                                    # profile_names=configuration.host_profile,
                                    # profile_build=configuration.build_profile,
                                    # settings=configuration.host_settings,
                                    # install_folder= installfolder)

class ConfigReader:
    def __init__(self, path):
        self.path = path
        self._configurations = [BuilderConfig()]
        self._signature = Signature()

    def read(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            if 'version' in data:
                self._signature.version = data['version']
            if 'user' in data:
                self._signature.user = data['user']
            if 'channel' in data:
                self._signature.channel = data['channel']
            if 'config' in data:
                self._configurations = []
                for p in data['config']:
                    configuration = BuilderConfig()
                    if 'hostprofile' in p:
                        configuration.host_profile = p['hostprofile']
                    if 'buildprofile' in p:
                        configuration.build_profile = p['buildprofile']
                    if 'hostsettings' in p:
                        configuration.host_settings = p['hostsettings']
                    if 'excludes' in p:
                        configuration.excludes= p['excludes']
                    if 'includes' in p:
                        configuration.includes= p['includes']
                    self._configurations.append(configuration)

    def get_configurations(self):
        return self._configurations


    def get_signature(self):
        return self._signature


def create_all(conan_packages, configurations):
    config_counter = 0
    for config in configurations:
        config_counter = config_counter + 1;
        eprint.ok(f"CONFIG {config_counter}")
        for package in conan_packages:
            if package.is_withing_scope(config):
                package.create(config)

    #relative_path = path.absolute()
    #eprint(package.pattern)

    # package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    ### conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    # TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    # print(f'SUCCESS: {package_pattern}')


def get_all_packages(root_path, signature=Signature()):
    conan_packages = []
    for path in Path(root_path).rglob('conanfile.py'):
        path = str(path.absolute())
        if "test_package" not in path:
            conan_packages.append(ConanPackage(signature, path))
    return conan_packages


def export_all(conan_packages):
    for package in conan_packages:
        package.export()


if __name__ == "__main__":
    current_file = os.getcwd()
    config_reader = ConfigReader(f'{current_file}/recipes/config-build.json')
    config_reader.read()
    packages = get_all_packages(current_file, config_reader.get_signature())
    export_all(packages)
    #create_all(packages,config_reader.get_configurations())
    packages[0].get_build_order(config_reader.get_configurations()[0])

