FROM mongo:6.0

# Install packages
RUN apt update -y; apt-get install nodejs npm supervisor netcat -y

# Setup app
RUN mkdir -p /app

# Add application
WORKDIR /app
COPY challenge .

# Install nodejs dependencies
RUN npm install -g yarn

# Install dependencies
RUN yarn

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Expose the port node-js is reachable on
EXPOSE 1337

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# Start the node-js application
ENTRYPOINT /entrypoint.sh