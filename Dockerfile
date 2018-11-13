FROM ubuntu:bionic

RUN apt-get update  && \
    apt-get install -y chromium-chromedriver python3 python3-pip && \
    ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver && \
    pip3 install pipenv

ADD . /home/app/

WORKDIR /home/app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pipenv install --three --system

ENTRYPOINT ["python3", "ichabod.py"]
