FROM  jojees/ubuntu:14.04

RUN mkdir /opt/lab \
    &&  /bin/bash -l -c "pip install --upgrade pip" \
    && /bin/bash -l -c "pip install --upgrade virtualenv" \
    && /bin/bash -l -c "pip install --upgrade nameko" \
    && /bin/bash -l -c "pip install --upgrade flask" \
    && /bin/bash -l -c "pip install --upgrade flasgger"

WORKDIR /opt/lab/api

#RUN /bin/bash -l -c "pip install twine"
CMD sleep 5; python api.py