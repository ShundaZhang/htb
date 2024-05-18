#!/bin/bash
docker rm -f web_stylish
docker build -t web_stylish . 

# Production
docker run --name=web_stylish --rm -p1337:1337 -it web_stylish