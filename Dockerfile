FROM bitnami/minideb:stretch
LABEL maintainer="guzmud"

WORKDIR /tmp

RUN install_packages slapd \
                     python3 \
                     python3-pip \
                     python3-setuptools \
                     supervisor

ADD requirements.txt /tmp/
RUN pip3 install -U pip
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir /npi
ADD slapd /npi/slapd/
ADD api /npi/api/
ADD supervisor /etc/supervisor/

# spoiler: next line is ugly
RUN service slapd stop

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "--nodaemon"]
