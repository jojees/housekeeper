FROM  jojees/ubuntu:14.04

RUN mkdir /opt/lab \
    &&  /bin/bash -l -c "pip install --upgrade pip" \
    && /bin/bash -l -c "pip install --upgrade virtualenv" \
    && /bin/bash -l -c "pip install --upgrade nameko" \
    && /bin/bash -l -c "pip install --upgrade yagmail" \
    && /bin/bash -l -c "pip install --upgrade XenApi"

WORKDIR /opt/lab/mgmt

#RUN /bin/bash -l -c "pip install twine"
CMD sleep 5; nameko run service --broker amqp://shnops:shnpass@rabbitmq.opslab.local