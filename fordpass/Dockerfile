  
ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

LABEL maintainer "SL <admin@loewe-web.com>"

RUN apk add --no-cache \
    	jq


COPY fordpass.py /
COPY run.sh /
RUN chmod a+x /run.sh
RUN chmod a+x /fordpass.py


CMD ["/run.sh"]