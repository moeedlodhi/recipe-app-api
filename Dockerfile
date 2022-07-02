FROM python:3.9-alpine3.13
LABEL maintainer="moeed"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV= false
RUN python -m venv new_env
RUN source new_env/bin/activate
RUN pip install -r /tmp/requirements.txt

ENV PATH = "/py/bin:$PATH"


