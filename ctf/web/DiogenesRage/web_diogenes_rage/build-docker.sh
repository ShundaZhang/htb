#!/bin/bash
docker rm -f web_diogenes_rage
docker build -t web_diogenes_rage . 
docker run --name=web_diogenes_rage --rm -p1337:1337 -it web_diogenes_rage
