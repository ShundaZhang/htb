#!/bin/bash
docker rm -f web_twodots_horror
docker build -t web_twodots_horror . 
docker run --name=web_twodots_horror --rm -p1337:1337 -it web_twodots_horror
