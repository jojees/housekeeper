FROM ubuntu:14.04

RUN sed -i 's/\(deb.*trusty-updates.*\)$/#\1/g' /etc/apt/sources.list \
    && echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
    && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
    && export TERM=xterm \
    && DEBIAN_FRONTEND=noninteractive \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get clean \
    && apt-get update \
    && apt-get install -y curl vim tree python-pip python-dev build-essential openssl python-dev libssl-dev \
    &&  /bin/bash -l -c "pip install --upgrade pip" \
    && /bin/bash -l -c "pip install --upgrade virtualenv"
#    && /bin/bash -l -c "pip install fabric" 

WORKDIR /opt/fabric-data
#
RUN /bin/bash -l -c "pip install twine"
