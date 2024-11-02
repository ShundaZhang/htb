# Use an official Debian base image
FROM debian:latest@sha256:1dc55ed6871771d4df68d393ed08d1ed9361c577cfeb903cd684a182e8a3e3ae

# Install necessary packages and python libraries
RUN apt-get update && \
    apt-get install -y supervisor php-fpm nginx samba && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure php-fpm, nginx, supervisord
COPY config/fpm.conf /etc/php/8.2/fpm/php-fpm.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Copy challenge and checker files
COPY challenge/app /www/app
COPY challenge/projects /www/projects
# COPY --chown=root:root challenge/checker.py /tmp

# Set up permissions
RUN chmod -R 777 /www
# RUN chmod 400 /tmp/checker.py
RUN chown -R www-data:www-data /var/lib/nginx

# Configure Samba
RUN echo "[app]" >> /etc/samba/smb.conf && \
    echo "path = /www/app" >> /etc/samba/smb.conf && \
    echo "browsable = yes" >> /etc/samba/smb.conf && \
    echo "writable = yes" >> /etc/samba/smb.conf && \
    echo "guest ok = yes" >> /etc/samba/smb.conf && \
    echo "read only = no" >> /etc/samba/smb.conf

# expose ports
EXPOSE 80 445

# Start supervisord
CMD service smbd start && /usr/bin/supervisord -c /etc/supervisord.conf
