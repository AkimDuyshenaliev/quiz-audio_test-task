FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg -y --no-install-recommends \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN 

WORKDIR /base/

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN set -ex && pipenv install --system --dev

COPY . .