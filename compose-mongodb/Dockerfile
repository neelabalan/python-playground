FROM python:3.8.8-alpine3.12

WORKDIR /app/

ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./app/ /app/

EXPOSE 5000
