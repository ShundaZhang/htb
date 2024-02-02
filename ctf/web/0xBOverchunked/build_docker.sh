#!/bin/bash

docker build --tag=web-overchunked . && \
docker run -p 1337:1337 --rm --name=web-overchunked -it web-overchunked