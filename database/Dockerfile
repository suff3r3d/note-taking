FROM postgres:latest

ENV POSTGRES_USER=chungdinh 
ENV POSTGRES_PASSWORD=18102005

VOLUME ["/var/log/db"]

COPY init.sql /docker-entrypoint-initdb.d