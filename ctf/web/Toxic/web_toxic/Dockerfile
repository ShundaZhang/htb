FROM alpine:3.13

# Setup user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Install system packages
RUN apk add --no-cache --update php7-fpm supervisor nginx

# Configure php-fpm and nginx
COPY config/fpm.conf /etc/php7/php-fpm.d/www.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Copy challenge files
COPY challenge /www

COPY flag /flag

# Setup permissions
RUN chown -R www:www /var/lib/nginx

# Expose the port nginx is listening on
EXPOSE 80

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# Start the node-js application
ENTRYPOINT [ "/entrypoint.sh" ]

# Populate database and start supervisord
CMD /usr/bin/supervisord -c /etc/supervisord.conf