#!/usr/bin/python
import os
from tools.disroopbuildhelper import run, chdir
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gitref", type=str, required=False, help="Pass Githubrefs with refs/tags/docker-v*.*.* to push")
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    ref = str(args.gitref)
    dockerversion="latest"
    if ref.startswith("refs/tags/docker-v"):
        dockerversion=ref.replace("refs/tags/docker-v", "")
    with chdir(os.path.dirname(os.path.realpath(__file__))):
        run(f'docker build --target ssh-server -t embedded-hipster-ssh:{dockerversion} .')
    if dockerversion != "latest":
        run(f'docker push embedded-hipster-ssh:{dockerversion}')
        
