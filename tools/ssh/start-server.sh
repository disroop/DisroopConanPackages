#!/bin/bash
docker run -p 22:22 disroop/embedded-hipster-ssh:latest
sshpass -p "pwd" ssh -o StrictHostKeyChecking=no user@172.17.0.1
ssh user@172.17.0.1 "setup && exit"
