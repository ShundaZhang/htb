#!/bin/bash
docker rm -f web_renderquest
docker build -t web_renderquest .
docker run --name=web_renderquest --rm -p1337:1337 -it web_renderquest