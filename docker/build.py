#!/usr/bin/python
import os
import argparse
import docker


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gitref", type=str, required=False, help="Pass Githubrefs with refs/tags/docker-v*.*.* to push")
    return parser.parse_args()


def docker_build_push(target, name, version, push=False):
    dockerhubrepo="disroop"
    client = docker.from_env()
    current_path = os.getcwd()
    client.images.build(path=current_path,target=target,tag=f'{dockerhubrepo}/{name}:{version}')
    if push:
        print(f"docker image {dockerhubrepo}/{name}:{version} push to server:")
        serveroutput=client.images.push(f"{dockerhubrepo}/{name}",tag=f'{version}')
        print(f'Server output: {serveroutput}')
        

if __name__ == '__main__':
    args = get_args()
    ref = str(args.gitref)
    dockerversion="latest"
    pushImage = False
    if ref.startswith("refs/tags/docker-v"):
        dockerversion=ref.replace("refs/tags/docker-v", "")
        pushImage = True
    docker_build_push('build-system','embedded-hipster',dockerversion,pushImage)
    docker_build_push('dev','embedded-hipster-dev',dockerversion,pushImage)
    docker_build_push('ssh-server','embedded-hipster-ssh',dockerversion,pushImage)
    docker_build_push('sonar','embedded-hipster-sonar',dockerversion,pushImage)
        
