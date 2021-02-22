FROM ubuntu:latest

RUN apt-get clean

RUN apt-get update

RUN apt-get install curl -y

RUN apt-get install python3.8 -y

RUN apt-get install python3.8 libpq-dev wait-for-it -y



RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"

RUN apt-get install unzip -y

RUN unzip awscliv2.zip

RUN ./aws/install


WORKDIR /code

COPY . .

RUN chmod +x script.sh

# RUN ./script.sh

# RUN chmod +x script1.sh


RUN apt-get install python3-pip -y

RUN pip3 install -r requirements.txt


ENV FLASK_APP=run.py

ENV FLASK_ENV=development

EXPOSE 8000


CMD ./script.sh