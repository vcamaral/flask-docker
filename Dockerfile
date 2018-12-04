FROM python:3.6-slim

LABEL maintaner "Vinicius Amaral <vcamaral@gmail.com>"

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py
