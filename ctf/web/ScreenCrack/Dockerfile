FROM php:8.1.10-alpine3.16

# Install system packages
RUN apk add --no-cache --update supervisor redis gcc libc-dev zip curl apache2 \
    php81-apache2 php81-redis php81-json php81-phar php81-iconv php81-mbstring \
    php81-sqlite3 php81-pdo_sqlite php81-xml php81-tokenizer php81-session \
    openssl php81-openssl php81-ctype php81-dom  php81-curl sqlite

# Download composer
RUN wget https://getcomposer.org/composer-2.phar -O /usr/local/bin/composer && chmod +x /usr/local/bin/composer

# Copy configuration files
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/httpd.conf /etc/apache2/httpd.conf
COPY config/redis.conf /etc/redis.conf
COPY config/job-runner.sh /job-runner.sh

# Copy App
COPY challenge /www

# Switch working environment
WORKDIR /www

# Copy flag
COPY flag /flag

# Install dependencies
RUN php /usr/local/bin/composer install
COPY challenge/.env /www/

RUN mkdir -p /www/var /www/public/static/exports

# Set permissions
RUN chown -R apache:apache /www

# Expose the port application is reachable on
EXPOSE 80

# Run supervisord
CMD /usr/bin/supervisord -c /etc/supervisord.conf
