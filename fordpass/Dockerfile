ARG BUILD_FROM
FROM $BUILD_FROM

ARG BUILD_ARCH
ARG BUILD_VERSION

LABEL maintainer "SL <admin@loewe-web.com>"


COPY fordpass.py /
COPY run.sh /
RUN chmod a+x /run.sh
RUN chmod a+x /fordpass.py


CMD ["/run.sh"]