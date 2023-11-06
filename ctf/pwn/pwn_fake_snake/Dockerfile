FROM python@sha256:7ded8135894464123583e8a000e6e88aa8a114a634a3eebe8556d69f7e03ffc3
RUN apt update && \
    apt install -y socat && \
    rm -rf /var/lib/apt/lists/*
COPY challenge/server.py /
COPY challenge/flag.txt /
USER 1000
CMD ["socat", "tcp-l:1337,reuseaddr,fork", "EXEC:python3 -S ./server.py"]

