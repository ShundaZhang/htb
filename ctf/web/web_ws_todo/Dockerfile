FROM ubuntu:22.04

# Install packages
RUN export DEBIAN_FRONTEND=noninteractive && \
    export DEBCONF_NONINTERACTIVE_SEEN=true && \
    apt update && apt install -y \
    nodejs \
    npm \
    supervisor \
    mysql-server \
    php \
    libnss3 libgbm1 libasound2

# setup mysql
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
COPY config/init.sql /tmp/init.sql
RUN /usr/sbin/mysqld & sleep 10 && mysql < /tmp/init.sql

# set root password
RUN echo "root:root" | chpasswd

# clean packages
RUN apt-get clean
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# Setup app
RUN mkdir -p /todo
RUN mkdir -p /htmltester

# Add application
COPY challenge/htmltester /htmltester

WORKDIR /todo
COPY challenge/todo .

# Install dependencies
RUN npm install

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Expose the port node-js is reachable on
EXPOSE 80
EXPOSE 8080

ENV MYSQL_USER web
ENV MYSQL_PASSWORD REDACTED
ENV SESSION_SECRET REDACTED
ENV USERNAME admin
ENV PASSWORD REDACTED
ENV FLAG HTB{test_flag}

# Start the node-js application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]