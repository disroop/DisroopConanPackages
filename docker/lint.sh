#!/usr/bin/env bash
clear
cat Dockerfile | docker run --rm -i hadolint/hadolint

