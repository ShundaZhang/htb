FROM alpine:3

# Install system packages
RUN apk add --no-cache --update wget apr-dev apr-util-dev gcc libc-dev \
    pcre-dev make musl-dev

# Download and extract httpd
RUN wget https://archive.apache.org/dist/httpd/httpd-2.4.55.tar.gz && tar -xvf httpd-2.4.55.tar.gz

WORKDIR httpd-2.4.55

# Compile httpd with desired modules
RUN ./configure \
    --prefix=/usr/local/apache2 \
    --enable-mods-shared=all \
    --enable-deflate \
    --enable-proxy \
    --enable-proxy-balancer \
    --enable-proxy-http \
    && make \
    && make install

# Move compiled httpd binary
RUN mv httpd /usr/local/bin

WORKDIR /

# Copy Apache config files
COPY conf/httpd.conf /tmp/httpd.conf
RUN cat /tmp/httpd.conf >> /usr/local/apache2/conf/httpd.conf

# Can't bind to port 80
RUN sed -i '/^Listen 80$/s/^/#/' /usr/local/apache2/conf/httpd.conf

# Copy challenge files
COPY challenge/frontend/src/. /usr/local/apache2/htdocs/
RUN mkdir /app

# Copy application and configuration files
COPY conf/. /app
COPY challenge/backend/src/. /app

# Install Python dependencies
RUN apk add --update --no-cache \
    g++ \
    python3 \
    python3-dev \
    build-base \
    linux-headers \
    py3-pip \
    && pip install -I --no-cache-dir -r /app/requirements.txt

# Add a system user and group
RUN addgroup -S uwsgi-group && adduser -S -G uwsgi-group uwsgi-user

# Fix permissions
RUN chown -R uwsgi-user:uwsgi-group /usr/local/apache2/logs \
    && chmod 755 /usr/local/apache2/logs \
    && touch /usr/local/apache2/logs/error.log \
    && chown uwsgi-user:uwsgi-group /usr/local/apache2/logs/error.log \
    && chmod 644 /usr/local/apache2/logs/error.log

# Switch user to uwsgi-user
USER uwsgi-user

# Expose Apache's port
EXPOSE 1337

# Run httpd and uwsgi
CMD ["sh", "/app/uwsgi/start_uwsgi.sh"]