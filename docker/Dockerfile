#################### Build-System Image ####################
FROM ubuntu:20.04 AS build-system

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-utils=2.0.5 \
    python3=3.8.2-0ubuntu2 \
    python3-pip \
    git=1:2.25.1-1ubuntu3 \
    clang=1:10.0-50~exp1 \
    clang-tidy=1:10.0-50~exp1 \
    iwyu=8.0-3build1 \
    cppcheck=1.90-4build1 \
    make=4.2.1-1.2 \
    llvm-11=1:11.0.0-2~ubuntu20.04.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/llvm-cov-11 /usr/bin/llvm-cov

#Remove python 2.7 us pyhton3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && rm -rf /usr/bin/pip \
    && ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip3 install --no-cache-dir conan==1.36.0
RUN pip3 install --no-cache-dir invoke==1.5.0
RUN pip3 install --no-cache-dir mumoco==0.2.1
#TODO: This is only temporary
RUN pip3 install --no-cache-dir eprint=0.0.5

# Add Setup Script
COPY setup.sh /run/setup.sh
RUN chmod +x /run/setup.sh \
    && ln -s /run/setup.sh /usr/bin/setup

#Install Cmake 3.19.2
RUN apt-get update

RUN apt-get install --no-install-recommends -y apt-transport-https ca-certificates gnupg software-properties-common wget

RUN wget -O --progress=dot:giga - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main' && apt-get update

RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal-rc main' && apt-get update

RUN apt-get install -y  kitware-archive-keyring && rm /etc/apt/trusted.gpg.d/kitware.gpg

RUN  apt-get install --no-install-recommends -y cmake

#################### sonar-scanner ####################
FROM build-system AS sonar

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \ 
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Sonar Build Wrapper
ARG BUILD_WRAPPER_HOME=/opt/build-wrapper-linux-x86
RUN wget -q -O /opt/build-wrapper-linux-x86.zip https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip \
    && unzip /opt/build-wrapper-linux-x86.zip -d /opt \
    && rm /opt/build-wrapper-linux-x86.zip
ENV BUILD_WRAPPER_HOME=${BUILD_WRAPPER_HOME} PATH=${BUILD_WRAPPER_HOME}:${PATH}
RUN ln -s ${BUILD_WRAPPER_HOME}/build-wrapper-linux-x86-64 ${BUILD_WRAPPER_HOME}/build-wrapper

# Sonar Scanner
RUN wget -q -O /opt/sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip \
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
    libncurses5 \
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
ARG FOLDER_JLINK=/opt/segger_jlink_v692
RUN wget --progress=dot:giga https://www.segger.com/downloads/jlink/${TAR_NAME} --directory-prefix=$TMP_JLINK_TGZ --post-data="accept_license_agreement=accepted"
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

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=dialog

RUN apt-get update && apt-get install --no-install-recommends -y \
    openssh-server \
    rsync

RUN  echo 'dev:pwd' | chpasswd

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

################################################################################################################################################################
# Clion Environment Image ######################################################################################################################################
################################################################################################################################################################
FROM dev AS clion
USER root

## Install OpenJDK-8
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    openjdk-8-jdk && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install --no-install-recommends -y ca-certificates-java=20190405ubuntu1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates -f;

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
#
ARG USERNAME=dev
ENV HOME=/home/${USERNAME}
USER ${USERNAME}
WORKDIR ${HOME}

ENV INTELLIJ_VERSION=CLion-211.7142.21
ENV IDEA_INSTALL_DIR="${INTELLIJ_VERSION}"
ENV IDEA_CONFIG_DIR=".${INTELLIJ_VERSION}"

ARG INTELLIJ_IDE_TAR=${INTELLIJ_VERSION}.tar.gz

RUN wget --progress=dot:giga https://download-cf.jetbrains.com/cpp/${INTELLIJ_IDE_TAR}
RUN tar xvf ${INTELLIJ_IDE_TAR} && \
    mv clion-* ${IDEA_INSTALL_DIR}  && \
    rm ${INTELLIJ_IDE_TAR}

ENV IDEA_PROJECT_DIR="CLionProjects"
RUN mkdir -p \
    ${HOME}/${IDEA_PROJECT_DIR} \
    ${HOME}/${IDEA_CONFIG_DIR}

VOLUME ${HOME}/${IDEA_PROJECT_DIR}
VOLUME ${HOME}/${IDEA_CONFIG_DIR}

#install plugins
ENV targetdir=${IDEA_INSTALL_DIR}/plugins

USER root
RUN apt-get update \
    && apt-get install --no-install-recommends -y unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
USER ${USERNAME}

RUN wget --progress=dot:giga https://plugins.jetbrains.com/files/11956/69344/Conan-1.2.0.zip &&  \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7499/120279/GitToolBox-203.5.10.zip && \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7495/83042/idea-gitignore-3.2.3.201.zip && \
wget --progress=dot:giga https://plugins.jetbrains.com/files/7125/119202/GrepConsole.zip && \
unzip "*.zip" -d $targetdir && \
rm *.zip

ENTRYPOINT ["/home/dev/CLion-211.7142.21/bin/clion.sh"]
