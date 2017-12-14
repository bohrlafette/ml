FROM ubuntu:16.04

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y python && \
  apt-get install -y python-pip && \
  apt-get install -y software-properties-common && \
  rm -rf /var/lib/apt/lists/*

# copy python scripts
COPY . /service

# install requirements
# this way when you build you won't need to install again
# and since COPY is cached we don't need to wait
COPY ./requirements.txt /tmp/requirements.txt

# Run the dependencies installer and then allow it to be run again if needed.
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

# for a flask server

EXPOSE 5000
#
CMD python /service/service.py
