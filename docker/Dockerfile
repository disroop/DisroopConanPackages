#################### Build-System Image ####################
FROM ubuntu:20.04 AS build-system

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-utils \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.1 \
    git=1:2.25.1-1ubuntu3 \
    clang=1:10.0-50~exp1 \
    ninja-build=1.10.0-1build1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#Remove python 2.7 us pyhton3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip3 install conan==1.36.0
RUN pip3 install mumoco==0.2.1
#TODO: This is only temporary
RUN pip3 install eprint

ADD setup.sh /run/setup.sh
RUN chmod +x /run/setup.sh \
    && ln -s /run/setup.sh /usr/bin/setup

#Install Cmake 3.19.2
RUN apt-get update

RUN apt-get install --no-install-recommends -y apt-transport-https ca-certificates gnupg software-properties-common wget

RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main' && apt-get update

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal-rc main' && apt-get update

RUN apt-get install kitware-archive-keyring && rm /etc/apt/trusted.gpg.d/kitware.gpg

RUN  apt-get install --no-install-recommends -y cmake

#################### dev-environment ####################
##### User: dev
##########################################################
FROM build-system AS dev
ENV DEBIAN_FRONTEND=noninteractive
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID
#
#Install specific devtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    vim=2:8.1.2269-1ubuntu5 \
    sudo=1.8.31-1ubuntu1.2\
    libncurses5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

#
# Install Pylint
RUN pip3 install pylint==2.6.0
#
#AddJlink Debugger Server
ARG TMP_JLINK_TGZ=/tmp
ARG TAR_NAME=JLink_Linux_x86_64.tgz
ARG FOLDER_JLINK=/opt/segger_jlink_v692
RUN wget https://www.segger.com/downloads/jlink/${TAR_NAME} --directory-prefix=$TMP_JLINK_TGZ --post-data="accept_license_agreement=accepted"
RUN mkdir ${FOLDER_JLINK} && tar -xzvf $TMP_JLINK_TGZ/$TAR_NAME -C ${FOLDER_JLINK} --strip 1
RUN ls /opt/segger_jlink_v692
RUN rm ${FOLDER_JLINK}/JLinkConfigExe
RUN rm ${FOLDER_JLINK}/JLinkGDBServerExe
RUN rm ${FOLDER_JLINK}/JLinkGUIServerExe
RUN rm ${FOLDER_JLINK}/JLinkRemoteServer
RUN rm ${FOLDER_JLINK}/JLinkRemoteServerCLExe
RUN rm ${FOLDER_JLINK}/JLinkRemoteServerExe
RUN rm ${FOLDER_JLINK}/JLinkRTTViewerExe
RUN rm ${FOLDER_JLINK}/JLinkSWOViewerExe
RUN rm ${FOLDER_JLINK}/JLinkRegistration
RUN rm ${FOLDER_JLINK}/JLinkRegistrationExe
RUN rm ${FOLDER_JLINK}/JLinkLicenseManager
RUN rm ${FOLDER_JLINK}/JLinkLicenseManagerExe
RUN rm -rf ${FOLDER_JLINK}/Samples
ENV PATH="${FOLDER_JLINK}:${PATH}"
#
# Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME
#
# Add sudo support for the non-root user
RUN apt-get install --no-install-recommends -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME
# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
#Switch back to dialog
ENV DEBIAN_FRONTEND=dialog

#################### SSH-Server Image ####################
##### User: dev
##### Password: pwd
##########################################################
FROM dev AS ssh-server

ENV DEBIAN_FRONTEND=dialog

RUN apt-get update && apt-get install --no-install-recommends -y \
    openssh-server \
    rsync

RUN  echo 'dev:pwd' | chpasswd

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
