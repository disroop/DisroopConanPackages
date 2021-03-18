#!/usr/bin/python
import os
from conans.client.conan_api import Conan
from conans.errors import ConanException
from collections import namedtuple
from pathlib import Path
from eprint import eprint

# print(os.environ['DOCKER_IMAGE'])
Package = namedtuple('Package', ['name', 'version', 'user', 'channel', 'path', 'pattern'])
conan_command_line, _, _ = Conan.factory()


def get_attribute(path, attribute,fail_on_invalid=False):
    attribute = str(attribute)
    try:
        conan_package = conan_command_line.inspect(path=f'{path}', attributes=[f'{attribute}'])
        return conan_package.get(attribute)
    except ConanException:
        if fail_on_invalid: 
            raise Exception(f"Attribute not found: {attribute} in {path} - {ConanException.message}")
    return "NONE"

def get_package_signature(path):
    conan_package = conan_command_line.inspect(path=f'{path}', attributes=["name"])
    name = get_attribute(path,'name',True)
    version = get_attribute(path,'version')
    user = get_attribute(path,'user')
    channel = get_attribute(path,'channel')
    path = str(path).replace("conanfile.py","")
    current_package = Package(name = name,
                              version = version, 
                              channel = channel,
                              user = user,
                              path = path,
                              pattern = f"{name}/{version}@{user}/{channel}")
    return current_package


def is_valid_recipe(excludes, path):
    path = str(path)
    for exclude in excludes:
        if exclude in path:
            return False
    return True


def run_build():
    current_path = os.getcwd()
    excludes = ["test_package"]
    #TODO: set environment variables
    
    for path in Path(current_path).rglob('conanfile.py'):
        if is_valid_recipe(excludes, path):
            relative_path = path.absolute()
            package = get_package_signature(relative_path)
            eprint(package.pattern)

    #package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    #
    conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    #TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    #print(f'SUCCESS: {package_pattern}')


if __name__ == "__main__":
    run_build()
