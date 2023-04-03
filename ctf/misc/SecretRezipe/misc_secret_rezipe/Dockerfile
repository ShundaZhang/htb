FROM node:16.3-alpine

# Install packages
RUN apk update && apk add supervisor zip

WORKDIR /app

COPY src/package.json .
RUN npm install --production

# Setup superivsord
COPY src/config/supervisord.conf /etc/supervisord.conf

# Expose the port node-js is reachable on
EXPOSE 1337

COPY src/src src

# COPY challenge/flag.txt /flag.txt

# Start the node-js application
CMD /usr/bin/supervisord -c /etc/supervisord.conf
