FROM alpine:3.18

RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Install system packages
RUN apk add --no-cache --update mariadb mariadb-client supervisor gcc musl-dev mariadb-connector-c-dev wget curl \
    supervisor nginx python3 py-pip python3-dev

# Install PHP dependencies
RUN apk add --no-cache --update php81 php81-fpm php81-mysqli

# Configure php-fpm and nginx
COPY config/fpm.conf /etc/php81/php-fpm.d/www.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Copy challenge files
COPY challenge/php_backend /www
COPY challenge/flask_frontend /app

# Setup permissions
RUN chown -R www:www /var/lib/nginx
RUN chown -R www:www /www

# Install requirements
RUN pip3 install -r /app/requirements.txt

# Expose the port nginx is listening on
EXPOSE 1337

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]