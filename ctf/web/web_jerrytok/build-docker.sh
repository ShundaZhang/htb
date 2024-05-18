#!/bin/bash
docker rm -f web_jerrytok
docker build -t web_jerrytok .
docker run --name=web_jerrytok --rm -p1337:1337 -it web_jerrytok