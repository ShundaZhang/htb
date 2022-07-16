FROM python:2-alpine

# Install system packages
RUN apk add --no-cache python3 supervisor

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install python requirements
RUN pip install -r requirements.txt

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]