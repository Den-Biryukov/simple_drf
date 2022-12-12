FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/simple_drf

COPY ./req.txt /usr/src/simple_drf/req.txt
RUN pip install -r /usr/src/simple_drf/req.txt

COPY . /usr/src/simple_drf

EXPOSE 8000
