#!/usr/bin/python
import os
import docker
from eprint import eprint
from conans.client.conan_api import Conan
from collections import namedtuple
import argparse

def get_args():
    cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=False, default=None, help="User credentials")
    parser.add_argument("--password", type=str, required=False, default=None, help="Access token")
    parser.add_argument("--upload", action="store_true", required=False, help="Upload to conan remote")
    return parser.parse_args()

def run_build(docker_image, container_command):
    client = docker.from_env()
    current_path = os.getcwd()
    try:
        retVal=client.containers.run(image=docker_image, command=container_command,remove=True, working_dir="/app", volumes={current_path: {'bind': '/app', 'mode': 'rw'}})
        retVal=retVal.decode('utf-8')
    except docker.errors.ContainerError as exc:
        exc = exc.stderr.decode('utf-8')
        eprint.error(f'Failed to run container:')
        eprint(exc)
        exit(1)
    eprint(f'{retVal}')
    eprint.ok("SUCCESS")


if __name__ == "__main__":
    args = get_args()
    command ="/bin/bash -c 'setup; ./build.sh'"
    run_build("disroop/embedded-hipster:0.4.0",command)
