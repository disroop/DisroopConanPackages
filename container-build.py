#!/usr/bin/python
import os
import docker
import argparse
import re


def get_args():
    cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=False,
                        default=None, help="User credentials")
    parser.add_argument("--password", type=str, required=False,
                        default=None, help="Access token")
    parser.add_argument("--upload", action="store_true",
                        required=False, help="Upload to conan remote")
    return parser.parse_args()


def run_build(docker_image, container_command):
    client = docker.from_env()
    current_path = os.getcwd()

    client = docker.from_env()
    container = client.containers.run(image=docker_image, command=container_command, remove=True,
                                      working_dir="/app", volumes={current_path: {'bind': '/app', 'mode': 'rw'}}, detach=True)
    hasError = False
    for line in container.logs(stream=True):
        text = str(line.strip())
        print(text)
        if re.search('ERROR', text, re.IGNORECASE):
            hasError = True
    if hasError:
        print(f'Failed to run container')
        exit(1)
    else:
        print("SUCCESS")


if __name__ == "__main__":
    args = get_args()
    bash_command = "./build.sh"
    if args.upload:
        bash_command += f"; mumoco remotes --username {args.username} --password {args.password}; mumoco upload disroop-conan"
    command = f"/bin/bash -c '{bash_command}'"
    run_build("disroop/embedded-hipster:0.6.12", command)
