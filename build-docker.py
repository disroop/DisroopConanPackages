#!/usr/bin/python
import os
from tools.disroopbuildhelper import run, chdir
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gitref", type=str, required=False, help="Pass Githubrefs with refs/tags/docker-v*.*.* to push")
    return parser.parse_args()


def docker_build_push(target, name, version, push=False):
    with chdir(os.path.dirname(os.path.realpath(__file__))):
        run(f'docker build --target {target} -t {name}:{version} .')
    if push:
        run(f'docker push {name}:{version}')
        print(f"docker image {name}:{version} pushed")

if __name__ == '__main__':
    args = get_args()
    ref = str(args.gitref)
    dockerversion="latest"
    pushImage = False
    if ref.startswith("refs/tags/docker-v"):
        dockerversion=ref.replace("refs/tags/docker-v", "")
        pushImage = True
    docker_build_push('ssh-server','embedded-hipster-ssh',dockerversion,pushImage)
        
