# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

# Update the list of available packages
RUN apt-get update

# Install supervisor, nodejs, npm, Python 3, pip, and virtualenv, then clean up to reduce image size
RUN apt-get install -y supervisor nodejs npm python3 python3-pip python3-venv \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set the working directory for the back-end component
WORKDIR /app/av

# Copy the Python requirements file into the container at /app/av
COPY ./challenge/av/requirements.txt /app/av

# Create a virtual environment in the container and activate it
RUN python3 -m venv /app/av/venv
ENV PATH="/app/av/venv/bin:$PATH"

# Install Python dependencies in the virtual environment
RUN pip3 install --upgrade pip && pip3 install -r /app/av/requirements.txt

# Copy the rest of the AV challenge's back-end application into the container
COPY ./challenge/av /app/av

# Change the working directory to the front-end application folder
WORKDIR /app/front-end

# Copy the front-end package.json to /app
COPY ./challenge/front-end/package.json /app

# Install front-end dependencies using npm
RUN npm install

# Copy the front-end source code into the container
COPY ./challenge/front-end /app/front-end

# Build the front-end using npm
RUN npm run build

# Inform Docker that the container listens on port 1337
EXPOSE 1337

# Copy the supervisord configuration file into the container
COPY ./config/supervisord.conf /etc/supervisord.conf

# Copy flag
COPY flag.txt /flag.txt

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]