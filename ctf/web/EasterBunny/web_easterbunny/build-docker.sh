#!/bin/bash
docker rm -f web_easterbunny
docker build --tag=web_easterbunny .
docker run -p 1337:80 -it --name=web_easterbunny web_easterbunny