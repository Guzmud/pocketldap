# Use bitnami/minideb
# sources: https://github.com/bitnami/minideb

FROM bitnami/minideb:stretch
MAINTAINER Guzmud <guzmud@nopunkintended.net>

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
ADD api /npi/api/

ENTRYPOINT ["python3"]
CMD ["/npi/api/pldapi.py"]
