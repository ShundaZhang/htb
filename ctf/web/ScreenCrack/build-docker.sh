#!/bin/bash
docker rm -f web_screencrack
docker build -t web_screencrack .
docker run --name=web_screencrack -v --rm -p 1337:80 -it web_screencrack