FROM python:3.8-slim
MAINTAINER MARKMOROZOV
WORKDIR /workdir
COPY . /workdir

RUN apt-get update && pip install --upgrade pip setuptools wheel poetry

RUN poetry config virtualenvs.create false --local && \
    poetry config virtualenvs.in-project false --local && \
    poetry install --no-dev

#CMD python -m retail_calculator.app
