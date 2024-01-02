FROM python:slim
# Add 
COPY src/firefox.rar /

# Install packages
RUN sed -i -e's/ main/ main contrib non-free/g' /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y python3-pip libgtk-3-0 libasound2 \
    curl libx11-xcb1 libdbus-glib-1-2 unrar supervisor  && \
    rm -rf /var/lib/apt/lists/* && \
    curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin 

# Extract firefox
RUN unrar x firefox.rar && rm firefox.rar
# Install dependencies
RUN pip install flask selenium
# Setup app
RUN mkdir -p /app
# Set working environment
WORKDIR /app
# Setup for remote website - not included here
# Add application
# COPY challenge .
#RUN mv /app/flag.txt /
# Setup superivsord
# COPY config/supervisord.conf /etc/supervisord.conf
# Expose the port flask is reachable on
# EXPOSE 1337
COPY bot.py /bot.py
# Start the python application
# CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
CMD ["python3", "/bot.py"]
