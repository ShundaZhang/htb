#!/bin/sh

docker build --tag=web-nothreshold . && \
docker run --log-driver=json-file --log-opt max-size=500m --log-opt max-file=3 -p 1337:1337 --rm --name=web-nothreshold -it web-nothreshold
