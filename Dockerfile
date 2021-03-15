#################### Build-System Image ####################
FROM ubuntu:20.04 AS build-system

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-utils \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.1 \
    git=1:2.25.1-1ubuntu3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

##Remove python 2.7 us pyhton3 as default
#RUN apt purge -y python\
#    && ln -s /usr/bin/python3 /usr/bin/python \
#    && ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip3 install -Iv conan==1.34.1

#Install Cmake 3.19.2
RUN apt-get update

RUN apt-get install --no-install-recommends -y apt-transport-https ca-certificates gnupg software-properties-common wget

RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main' && apt-get update

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal-rc main' && apt-get update

RUN apt-get install kitware-archive-keyring && rm /etc/apt/trusted.gpg.d/kitware.gpg

RUN  apt-get install --no-install-recommends -y cmake

#################### SSH-Server Image ####################
##### User: ssh
##### Password: pwd
##########################################################
FROM build-system AS ssh-server

ENV DEBIAN_FRONTEND=dialog

RUN apt-get update && apt-get install --no-install-recommends -y \
    openssh-server \
    rsync

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 user 

RUN  echo 'user:pwd' | chpasswd

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]