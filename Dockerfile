FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

COPY ./app .
