#!/bin/bash
docker build -t web_toxic .
docker run --name=web_toxic --rm -p1337:80 -it web_toxic