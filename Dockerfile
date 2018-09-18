## Debian container for oldmanreffi.com project
FROM debian

MAINTAINER Mark Gagnon

RUN apt-get update
RUN apt-get install python3 python3-pip python-dev postgresql postgresql-contrib
RUN pip3 install django psycopg2
