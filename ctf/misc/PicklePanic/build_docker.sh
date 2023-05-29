#!/bin/sh

docker build . -t misc_picklepanic && \
    docker run -it -p1337:1337 misc_picklepanic
