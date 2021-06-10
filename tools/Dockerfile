FROM ubuntu:20.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    rsync=3.1.3-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
