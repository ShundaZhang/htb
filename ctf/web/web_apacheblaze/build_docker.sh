#!/bin/sh
docker build --tag=apacheblaze . && \
docker run -p 1337:1337 -it --rm --name=apacheblaze apacheblaze 
