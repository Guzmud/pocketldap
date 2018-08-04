FROM bitnami/minideb:stretch
LABEL maintainer="guzmud"

WORKDIR /tmp

RUN install_packages slapd \
                     python3 \
                     python3-pip \
                     python3-setuptools \
                     python3-dev \
                     build-essential \
                     supervisor

# spoiler: next line is ugly
RUN service slapd stop

ADD requirements.txt /tmp/
RUN pip3 install -U pip
RUN pip3 install -r /tmp/requirements.txt

RUN rm -r /etc/ldap/slapd.d/
ADD slapd.d /etc/ldap/slapd.d/
ADD api /npi/api/
ADD supervisor /etc/supervisor/
RUN mkdir -p /npi/pldap

EXPOSE 80/tcp

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "--nodaemon"]
