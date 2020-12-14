ARG BUILD_FROM
FROM $BUILD_FROM

ARG BUILD_ARCH
ARG BUILD_VERSION

LABEL maintainer "SL <admin@loewe-web.com>"


COPY fordpass.py /fordpass.py
COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]