FROM python:3.10.6-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD . /code
