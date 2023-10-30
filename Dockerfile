#pull official base image
FROM python:3.10-slim

RUN apt-get update

RUN apt-get install python3-dev build-essential -y

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ENV PATH="/opt/venv/bin:PATH"

RUN python -m virtualenv /opt/venv

# Sanal ortamı aktive et
ENV PATH="/opt/venv/bin:$PATH"

# Gereklilikleri yükle
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


# Uygulama kodunu kopyala
COPY . /srv/app
WORKDIR /srv/app



