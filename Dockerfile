FROM python:3.8-slim-bookworm

RUN sed -i 's|deb.debian.org|archive.debian.org|g' /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN JishuDeveloper /Ultra-Forward-Bot
WORKDIR /Ultra-Forward-Bot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"] 
