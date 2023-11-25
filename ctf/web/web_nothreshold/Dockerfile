FROM alpine:edge

RUN apk update && apk upgrade && apk add --no-cache \
    pcre \
    pcre-dev \
    make \
    gcc \
    musl-dev \
    linux-headers \
    python3 \
    python3-dev \
    py3-pip \
    sqlite \
    && rm -rf /var/cache/apk/*

WORKDIR /tmp

RUN wget https://www.haproxy.org/download/2.8/src/haproxy-2.8.3.tar.gz && \
    tar zxvf haproxy-*.tar.gz && \
    cd haproxy-* && \
    make TARGET=linux-musl && \
    make install
RUN rm -rf /tmp/haproxy-*

RUN mkdir -p /etc/haproxy
RUN mkdir -p /opt/www/app

COPY conf/haproxy.cfg /etc/haproxy/haproxy.cfg
COPY conf/requirements.txt /opt/www/app
COPY conf/uwsgi.ini /opt/www/app
COPY challenge/. /opt/www/app

WORKDIR /opt/www/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install -I --no-cache-dir -r requirements.txt 

RUN addgroup -S www-group && adduser -S -G www-group www-user && \
    chown -R www-user:www-group /opt/www/

WORKDIR /

COPY entrypoint.sh .
RUN chown www-user:www-group entrypoint.sh

RUN chmod 600 entrypoint.sh
RUN chmod +x entrypoint.sh

USER www-user

EXPOSE 1337

CMD ["./entrypoint.sh"]