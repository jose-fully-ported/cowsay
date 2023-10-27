# syntax = docker/dockerfile:1.5
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt && echo "subdir dockerfile"

COPY . .
