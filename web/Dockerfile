FROM  jojees/ubuntu:14.04

RUN mkdir /opt/lab \
    && /bin/bash -l -c "pip install --upgrade pip" \
    && curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - \
    && apt-get install -y nodejs git \
    && /bin/bash -l -c "pip install --upgrade virtualenv" \
    && /bin/bash -l -c "pip install --upgrade flask"

WORKDIR /opt/lab/web
ADD startup.sh /startup.sh

RUN chmod +x /startup.sh \
    && /bin/bash -l -c "npm install -g bower"

#CMD python housekeeper_web/web.py
CMD /startup.sh

RUN apt-get install -y mysql