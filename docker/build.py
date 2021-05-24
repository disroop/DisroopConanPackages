#!/usr/bin/python
import argparse
import os

import docker


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gitref", type=str, required=False,
                        help="Pass Githubrefs with refs/tags/docker-v*.*.* to push")
    return parser.parse_args()


def docker_build_push(target, name, version, push=False):
    dockerhub_repo = "disroop"
    client = docker.from_env()
    current_path = os.getcwd()
    client.images.build(path=current_path, target=target, tag=f'{dockerhub_repo}/{name}:{version}')
    if push:
        print(f"docker image {dockerhub_repo}/{name}:{version} push to server:")
        server_output = client.images.push(f"{dockerhub_repo}/{name}", tag=f'{version}')
        print(f'Server output: {server_output}')


if __name__ == '__main__':
    args = get_args()
    ref = str(args.gitref)
    docker_version = "latest"
    pushImage = False
    if ref.startswith("refs/tags/docker-v"):
        docker_version = ref.replace("refs/tags/docker-v", "")
        pushImage = True
    docker_build_push('build-system', 'embedded-hipster', docker_version, pushImage)
    docker_build_push('dev', 'embedded-hipster-dev', docker_version, pushImage)
    docker_build_push('ssh-server', 'embedded-hipster-ssh', docker_version, pushImage)
    docker_build_push('sonar', 'embedded-hipster-sonar', docker_version, pushImage)
