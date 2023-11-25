#!/bin/sh

docker build --tag=web-nothreshold . && \
docker run -p 1337:1337 --rm --name=web-nothreshold -it web-nothreshold