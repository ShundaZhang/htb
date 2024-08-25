FROM python:3.11-alpine

# Install dependencies
RUN apk add --update --no-cache supervisor chromium chromium-chromedriver

# Add chromium to PATH
ENV PATH="/usr/lib/chromium:${PATH}"

# Copy flag
COPY flag.txt /flag.txt

# Upgrade pip
RUN python -m pip install --upgrade pip

# Setup app
RUN mkdir -p /app

# Add application
WORKDIR /app
COPY challenge .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Setup supervisord
COPY conf/supervisord.conf /etc/supervisord.conf

# Expose port
EXPOSE 1337

# Start supervisor
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]