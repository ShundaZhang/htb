FROM alpine:3

# Setup user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Install system packages
RUN apk add --no-cache --update supervisor openssl curl apache2 \
    build-base pkgconfig libxml2-dev openssl-dev libzip-dev

# Install php dependencies
RUN apk add --no-cache --update coreutils gettext php-cgi php-fpm php-ctype php-curl php-dom php-gd \
    php-iconv php-json php-intl php-fileinfo php-mbstring php-opcache php-openssl php-pdo \
    php-pdo_mysql php-mysqli php-xml php-xsl php-zlib php-phar php-tokenizer php-session \
    php-simplexml php-zip php-xmlwriter php-sodium php-pecl-apcu make 

# Fix iconv library
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

WORKDIR /

# Download composer
RUN wget https://getcomposer.org/composer-2.phar -O /usr/local/bin/composer && chmod +x /usr/local/bin/composer

# Configure apache2 & supervisor
COPY config/httpd.conf /etc/apache2/httpd.conf
COPY config/supervisord.conf /etc/supervisord.conf

# Setup permissions
COPY --chown=www:www challenge /www

# Switch working environment
WORKDIR /www

# Add readflag binary
COPY readflag.c /
RUN gcc -o /readflag /readflag.c && chmod 4755 /readflag && rm /readflag.c

# Copy flag
COPY flag /root/flag

# Install dependencies
RUN php /usr/local/bin/composer install
RUN chown -R www:www /www/var /www/vendor

# Expose web app
EXPOSE 1337

# Run supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]