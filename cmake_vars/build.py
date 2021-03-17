#!/usr/bin/python
import os
import docker
from eprint import eprint
from conans.client.conan_api import Conan
from collections import namedtuple

# print(os.environ['DOCKER_IMAGE'])


def run_build():
    client = docker.from_env()
    current_path = os.getcwd()
    try:
        retVal=client.containers.run(image="disroop/embedded-hipster:latest", command=f"./conan-build.py",remove=True, working_dir="/app", volumes={current_path: {'bind': '/app', 'mode': 'rw'}})
        retVal=retVal.decode('utf-8')
    except docker.errors.ContainerError as exc:
        exc = exc.stderr.decode('utf-8')
        eprint.error(f'Failed to run container:')
        eprint(exc)
        exit(1)
    eprint(f'{retVal}')
    eprint.ok("SUCCESS")


if __name__ == "__main__":
    run_build()
