#!/bin/sh
docker build . -t pwn_superfast && \
docker run -p1337:1337 -it pwn_superfast
