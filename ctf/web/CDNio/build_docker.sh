#!/bin/sh

docker build --tag=web-cdnio . && \
docker run -p 1337:1337 --rm --name=web-cdnio -it web-cdnio