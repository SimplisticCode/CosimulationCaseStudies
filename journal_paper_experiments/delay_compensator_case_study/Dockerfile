FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3 python3-pip

WORKDIR /casestudy/Examples

RUN python3 -m pip install --upgrade pip

RUN pip install wheel

COPY Examples/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      default-jre-headless \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
