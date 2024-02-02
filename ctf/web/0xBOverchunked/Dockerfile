FROM alpine:3.9

RUN apk update && apk upgrade && apk add --no-cache \
    sqlite \
    sqlite-dev \
    supervisor \
    apache2 \
    php \
    php-apache2 \
    php-pdo_sqlite

RUN mkdir /opt/app
WORKDIR /opt/app

COPY challenge/. .

RUN sqlite3 /opt/app/db/chunked.db < /opt/app/db/init.sql

COPY conf/httpd.conf /etc/apache2/httpd.conf
COPY conf/supervisord.conf /etc/supervisord.conf

EXPOSE 1337

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
