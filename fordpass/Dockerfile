  
ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

LABEL maintainer "SL <admin@loewe-web.com>"

RUN apk add --no-cache jq
RUN apk add --no-cache py-pip
RUN apk add --no-cache python3
RUN apk add --no-cache python3-dev

RUN pip install -U pip
RUN pip3 install -U pip
RUN pip install -U virtualenv

RUN pip3 install -U requests
RUN pip3 install -U python-daemon


COPY fordpass.py /
COPY run.sh /
RUN chmod a+x /run.sh
RUN chmod a+x /fordpass.py


CMD ["/run.sh"]