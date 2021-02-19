FROM ubuntu:latest

RUN apt-get clean

RUN apt-get update

RUN apt-get install python3.8 -y

RUN apt-get install python3.8 libpq-dev wait-for-it -y

WORKDIR /code

COPY . .


RUN apt-get install python3-pip -y

RUN pip3 install -r requirements.txt


ENV FLASK_APP=run.py

ENV FLASK_ENV=development

CMD [ "flask", "run", "-h", "0.0.0.0" ]