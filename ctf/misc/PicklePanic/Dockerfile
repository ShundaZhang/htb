FROM python@sha256:4949a0cd8c491c3ab21132533a487dbe8fb6dae586b667ed4b3d19c8b127187e
RUN apk add --no-cache socat
RUN adduser --disabled-password --no-create-home picklepanic
COPY challenge /challenge/
WORKDIR /challenge
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]
