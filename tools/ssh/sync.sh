#!/bin/bash
FILE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
HOME_DIR=$FILE_DIR/../..
rsync -r $HOME_DIR user@172.17.0.1:/app