#!/usr/bin/python
import os
from conans.client.conan_api import Conan
from conans.errors import ConanException
from collections import namedtuple
from pathlib import Path
from eprint import eprint
import json

# print(os.environ['DOCKER_IMAGE'])
Package = namedtuple('Package', ['name', 'version', 'user', 'channel', 'path', 'pattern'])
CreateConfig = namedtuple('CreateConfig', ['hostprofile', 'buildprofile', 'hostsettings', 'excludes', 'includes', 'version','user','channel'])
conan_command_line, _, _ = Conan.factory()

def get_build_config(path):
    configurations = []
    with open(path) as json_file:
        data = json.load(json_file)
        for p in data['config']:
            excludefolders = ["test_package"]
            if 'excludes' in p:
                excludefolders = p['excludes']
            includefolders = []
            if 'includes' in p:
                includefolders = p['includes']
            config = CreateConfig(hostprofile = p['hostprofile'],
                              buildprofile = p['buildprofile'], 
                              hostsettings = p['hostsettings'],
                              excludes = excludefolders,
                              includes = includefolders,
                              version = p['version'],
                              user=p['user'],
                              channel=p['channel'])
            configurations.append(config)
    return configurations
            

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

def check_includes(includes,path):
    if len(includes) > 0: 
        for include in includes:
            if include in path:
                return True
        return False
    return True
    
def is_valid_recipe(includes, excludes, path):
    path = str(path)
    if check_includes(includes,path) == False:
        return False
    for exclude in excludes:
        if exclude in path:
            return False
    return True


def run_build(config):
    current_path = os.getcwd()
    #excludes = ["test_package"]
    #TODO: set environment variables
    
    for path in Path(current_path).rglob('conanfile.py'):
        if is_valid_recipe(config.includes,config.excludes, path):
            relative_path = path.absolute()
            package = get_package_signature(relative_path)
            eprint(package.pattern)

    #package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    ### conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    #TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    #print(f'SUCCESS: {package_pattern}')

if __name__ == "__main__":
    current_file = os.getcwd()
    build_configs = get_build_config(f'{current_file}/recipes/config-build.json')
    cnt=0;
    for config in build_configs:
        cnt=cnt+1;
        eprint.ok(f"CONFIG {cnt}")
        run_build(config)
