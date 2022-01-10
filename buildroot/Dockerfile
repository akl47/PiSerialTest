FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    bash \
    bc \
    binutils \
    build-essential \
    bzip2 \
    cpio \
    g++ \
    gcc \
    git \
    gzip \
    locales \
    libncurses5-dev \
    libdevmapper-dev \
    libsystemd-dev \
    make \
    mercurial \
    whois \
    patch \
    perl \
    python \
    rsync \
    sed \
    tar \
    vim \ 
    unzip \
    wget \
    bison \
    flex \
    libssl-dev \
    libfdt-dev \
    nano

# Sometimes Buildroot need proper locale, e.g. when using a toolchain
# based on glibc.
RUN locale-gen en_US.utf8

RUN git clone git://git.buildroot.net/buildroot --depth=1 --branch=2021.02.x /root/buildroot

# WORKDIR /root/buildroot

# ENV O=/buildroot_output

# RUN touch kernel.config

# VOLUME /root/buildroot/dl
# VOLUME /buildroot_output

RUN ["/bin/bash"]
# docker build -t "akl47/buildroot"
#docker run -it --rm -v $(pwd):/root/buildroot "akl47/buildroot"