  
ARG BUILD_FROM
FROM $BUILD_FROM


LABEL maintainer "SL <admin@loewe-web.com>"

RUN apk add --no-cache \
    	jq \
        py-pip \
	python \
	python-dev \
	python3 \
	python3-dev\
 && pip install -U pip \
 && pip3 install -U pip \
 && pip install -U virtualenv


COPY fordpass.py /
COPY run.sh /
RUN chmod a+x /run.sh
RUN chmod a+x /fordpass.py


CMD ["/run.sh"]