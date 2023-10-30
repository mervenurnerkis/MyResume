#pull official base image
FROM python:3.10-slim

RUN apt-get update

RUN apt-get install python3-dev build-essential -y

# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:PATH"

RUN python -m virtualenv $VIRTUAL_ENV

# Sanal ortamı aktive et
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Gereklilikleri yükle
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Uygulama kodunu kopyala
COPY . /srv/app
WORKDIR /srv/app



