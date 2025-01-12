FROM alpine:latest

RUN apk update && apk upgrade && apk add --no-cache \
    nginx \
    python3 \
    sqlite \
    py3-pip \
    openssl \
    && rm -rf /var/cache/apk/*

ENV PATH="/venv/bin:$PATH"

WORKDIR /www

COPY conf/requirements.txt .

RUN python3 -m venv /venv

RUN pip3 install --no-cache-dir -r requirements.txt

COPY challenge/ .

COPY conf/nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /
RUN chmod 600 /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]
