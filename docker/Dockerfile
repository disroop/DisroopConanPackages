#################### Build-System Image ####################
FROM ubuntu:20.04 AS build-system

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install --no-install-recommends -y \
    ca-certificates=20210119~20.04.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY sources.list /etc/apt/sources.list 


ENV DEBIAN_FRONTEND=noninteractive

ENV AM_I_IN_A_DISROOP_DOCKER_CONTAINER Yes


RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-utils=2.0.6 \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.5 \
    git=1:2.25.1-1ubuntu3 \
    clang-10=1:10.0.0-4ubuntu1 \
    clang-tidy-10=1:10.0.0-4ubuntu1\
    clang-format-10=1:10.0.0-4ubuntu1 \
    iwyu=8.0-3build1 \
    cppcheck=1.90-4build1 \
    make=4.2.1-1.2 \
    llvm-11=1:11.0.0-2~ubuntu20.04.1 \
    gdb=9.2-0ubuntu1~20.04 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#Set sym links to tools
RUN ln -s /usr/bin/llvm-cov-11 /usr/bin/llvm-cov \
    && ln -s /usr/bin/clang-10 /usr/bin/clang \
    && ln -s /usr/bin/clang++-10 /usr/bin/clang++\
    && ln -s /usr/bin/clang-tidy-10 /usr/bin/clang-tidy \
    && ln -s /usr/bin/clang-format-10 /usr/bin/clang-format \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && rm -rf /usr/bin/pip \
    && ln -s /usr/bin/pip3 /usr/bin/pip

#Set Install PIP Packages
RUN pip3 install --no-cache-dir conan==1.36.0 invoke==1.5.0 mumoco==0.2.1

# Add Setup Script
COPY setup.sh /run/setup.sh
RUN chmod +x /run/setup.sh \
    && ln -s /run/setup.sh /usr/bin/setup

#Install Cmake 3.20.5
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget=1.20.3-1ubuntu1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget --progress=dot:giga -qO- "https://disroop.jfrog.io/artifactory/third-party-mirror/cmake-3.20.5-linux-x86_64.tar.gz" | tar --strip-components=1 -xz -C /usr/local

#################### sonar-scanner ####################
FROM build-system AS sonar

RUN apt-get update && apt-get install --no-install-recommends -y \
    unzip=6.0-25ubuntu1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Sonar Build Wrapper
ARG BUILD_WRAPPER_HOME=/opt/build-wrapper-linux-x86
RUN wget --progress=dot:giga -O /opt/build-wrapper-linux-x86.zip https://disroop.jfrog.io/artifactory/third-party-mirror/sonar-cloud-build-wrapper-linux-x86.zip \
    && unzip /opt/build-wrapper-linux-x86.zip -d /opt \
    && rm /opt/build-wrapper-linux-x86.zip
ENV BUILD_WRAPPER_HOME=${BUILD_WRAPPER_HOME} PATH=${BUILD_WRAPPER_HOME}:${PATH}
RUN ln -s ${BUILD_WRAPPER_HOME}/build-wrapper-linux-x86-64 ${BUILD_WRAPPER_HOME}/build-wrapper

# Sonar Scanner
RUN wget --progress=dot:giga -O /opt/sonar-scanner-cli.zip https://disroop.jfrog.io/artifactory/third-party-mirror/sonar-scanner-cli-4.6.2.2472-linux.zip \
    && unzip /opt/sonar-scanner-cli.zip -d /opt \
    && rm /opt/sonar-scanner-cli.zip

ARG SONAR_SCANNER_HOME=/opt/sonar-scanner-4.6.2.2472-linux
ENV SONAR_SCANNER_HOME=${SONAR_SCANNER_HOME} PATH=${SONAR_SCANNER_HOME}/bin:${PATH}

#################### dev-environment ####################
##### User: dev
##########################################################
FROM sonar AS dev
ENV DEBIAN_FRONTEND=noninteractive
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID
#
#Install specific devtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    vim=2:8.1.2269-1ubuntu5 \
    sudo=1.8.31-1ubuntu1.2\
    libncurses5=6.2-0ubuntu2 \
    ssh=1:8.2p1-4 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

#
# Install Pylint
RUN pip3 install --no-cache-dir pylint==2.6.0
#
#AddJlink Debugger Server
ARG TMP_JLINK_TGZ=/tmp
ARG TAR_NAME=JLink_Linux_x86_64.tgz
ARG FOLDER_JLINK=/opt/segger-jlink
RUN wget --progress=dot:giga https://disroop.jfrog.io/artifactory/third-party-mirror/JLink_Linux_V750_x86_64.tgz --directory-prefix=$TMP_JLINK_TGZ \
    && mkdir ${FOLDER_JLINK} && tar -xzvf $TMP_JLINK_TGZ/JLink_Linux_V750_x86_64.tgz -C ${FOLDER_JLINK} --strip 1 \
    && rm ${FOLDER_JLINK}/JLinkConfigExe \
    && rm ${FOLDER_JLINK}/JLinkGDBServerExe \
    && rm ${FOLDER_JLINK}/JLinkGUIServerExe \
    && rm ${FOLDER_JLINK}/JLinkRemoteServer \
    && rm ${FOLDER_JLINK}/JLinkRemoteServerCLExe \
    && rm ${FOLDER_JLINK}/JLinkRemoteServerExe \
    && rm ${FOLDER_JLINK}/JLinkRTTViewerExe \
    && rm ${FOLDER_JLINK}/JLinkSWOViewerExe \
    && rm ${FOLDER_JLINK}/JLinkRegistration \
    && rm ${FOLDER_JLINK}/JLinkRegistrationExe \
    && rm ${FOLDER_JLINK}/JLinkLicenseManager \
    && rm ${FOLDER_JLINK}/JLinkLicenseManagerExe \
    && rm -rf ${FOLDER_JLINK}/Samples
ENV PATH="${FOLDER_JLINK}:${PATH}"
#
# Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME
#
# Add sudo support for the non-root user
RUN apt-get install --no-install-recommends -y sudo=1.8.31-1ubuntu1.2 \
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

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=dialog

RUN apt-get update && apt-get install --no-install-recommends -y \
    openssh-server=1:8.2p1-4ubuntu0.2 \
    rsync=3.1.3-8

#Define  new password
RUN  echo 'dev:pwd' | chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

################################################################################################################################################################
# Clion Environment Image ######################################################################################################################################
################################################################################################################################################################
FROM dev AS clion

## Install OpenJDK-8
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    openjdk-8-jdk=8u292-b10-0ubuntu1~20.04 \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Fix certificate issues
RUN apt-get update  \
    && apt-get install --no-install-recommends -y \
    ca-certificates-java=20190405ubuntu1 \
    && update-ca-certificates -f \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
#
ARG USERNAME=dev
ENV HOME=/home/${USERNAME}
USER ${USERNAME}
WORKDIR ${HOME}

ENV CLION_VERSION=CLion-2021.1.2
ENV CLION_INSTALL_DIR="${CLION_VERSION}"
ENV CLION_CONFIG_DIR=".${CLION_VERSION}"

ARG CLION_IDE_TAR=${CLION_VERSION}.tar.gz

RUN wget --progress=dot:giga https://download-cf.jetbrains.com/cpp/${CLION_IDE_TAR}\
    && tar xvf ${CLION_IDE_TAR} \
    &&  mv clion-* ${CLION_INSTALL_DIR} \
    && rm ${CLION_IDE_TAR}

ENV CLION_PROJECT_DIR="CLionProjects"
RUN mkdir -p \
    ${HOME}/${CLION_PROJECT_DIR} \
    ${HOME}/${CLION_CONFIG_DIR}

VOLUME ${HOME}/${CLION_PROJECT_DIR}
VOLUME ${HOME}/${CLION_CONFIG_DIR}

#install plugins
ENV targetdir=${CLION_INSTALL_DIR}/plugins

USER root
RUN apt-get update \
    && apt-get install --no-install-recommends -y unzip=6.0-25ubuntu1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
USER ${USERNAME}

RUN wget --progress=dot:giga https://plugins.jetbrains.com/files/11956/69344/Conan-1.2.0.zip &&  \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7499/120279/GitToolBox-203.5.10.zip && \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7495/83042/idea-gitignore-3.2.3.201.zip && \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7125/119202/GrepConsole.zip && \
unzip "./*.zip" -d $targetdir && \
rm ./*.zip

ENTRYPOINT ["/home/dev/CLion-2021.1.2/bin/clion.sh"]
