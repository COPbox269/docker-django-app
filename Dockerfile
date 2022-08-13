# syntax=docker/dockerfile:1

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED=1

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /code/