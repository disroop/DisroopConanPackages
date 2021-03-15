#!/usr/bin/python
import os
from tools.disroopbuildhelper import run, chdir

if __name__ == '__main__':
    with chdir(os.path.dirname(os.path.realpath(__file__))):
        run(f'docker build --target ssh-server -t embedded-hipster-ssh:latest .')
