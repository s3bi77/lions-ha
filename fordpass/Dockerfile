FROM python:3

LABEL maintainer "SL <admin@loewe-web.com>"


COPY fordpass.py /
COPY run.sh /
RUN chmod a+x /run.sh
RUN chmod a+x /fordpass.py


CMD ["/run.sh"]