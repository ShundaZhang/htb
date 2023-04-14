FROM node:current-buster-slim

# Install Chrome
RUN apt update \
    && apt install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt update \
    && apt install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 libxshmfence-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install varnish & supervisord
RUN apt update \
    && wget -q -O - https://packagecloud.io/varnishcache/varnish60lts/gpgkey | apt-key add - \
    && sh -c 'echo "deb https://packagecloud.io/varnishcache/varnish60lts/debian/ buster main" >> /etc/apt/sources.list.d/varnishcache_varnish60lts.list' \
    && apt update \
    && apt install -y varnish apt-transport-https supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN dd if=/dev/urandom of=/etc/varnish/secret count=1

# Setup varnish and supervisord
COPY ./config/cache.vcl /etc/varnish/default.vcl
COPY ./config/supervisord.conf /etc/supervisor/supervisord.conf

# Setup app
RUN mkdir -p /app

# Add application
WORKDIR /app
COPY --chown=www-data:www-data challenge .

# Install dependencies
RUN yarn

# Expose the port application is reachable on
EXPOSE 80

# Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]