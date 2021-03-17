#!/usr/bin/python
import os
from conans.client.conan_api import Conan
from collections import namedtuple

# print(os.environ['DOCKER_IMAGE'])
Package = namedtuple('Package', ['name', 'version', 'user', 'channel'])
conan_command_line, _, _ = Conan.factory()


def get_package_signature():
    current_path = os.getcwd()
    conan_package = conan_command_line.inspect(path=f'{current_path}', attributes=["name", "version", "channel", "user"])
    current_package = Package(conan_package.get('name'), conan_package.get('version'), conan_package.get('user'),
                              conan_package.get('channel'))
    return current_package


def run_build():
    current_path = os.getcwd()

    package_signature = get_package_signature()
    package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    
    conan_command_line.create(current_path,test_build_folder=f'/tmp/{package_pattern}/tbf')#TODO:profiles_names =HOST, profiles_build=build
    #conan_command_line.authenticate()
    #conan_command_line.remote_add()
    #conan_command_line.upload(package_pattern)
    print(f'SUCCESS: {package_pattern}')

if __name__ == "__main__":
    run_build()
