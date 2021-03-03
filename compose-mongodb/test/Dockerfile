FROM python:3.8.8-alpine3.12

WORKDIR /test/

ADD ./requirements.txt /test/
RUN pip install -r requirements.txt

ADD ./requirements-dev.txt /test/
RUN pip install -r requirements-dev.txt 

ADD ./ /test/