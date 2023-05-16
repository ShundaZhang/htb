FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat

WORKDIR /app
COPY challenge .

RUN useradd -m ctf
USER ctf

EXPOSE 5000
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:/app/ancient_interface"]
