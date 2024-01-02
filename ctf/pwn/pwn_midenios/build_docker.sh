#!/bin/bash

docker build --tag=pwn_midenios . && \
docker run -it --rm --name=pwn_midenios pwn_midenios
