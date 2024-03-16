#!/bin/bash
docker rm -f web_insomnia
docker build --no-cache --tag=web_insomnia .
docker run -p 1337:80 --rm --name=web_insomnia -it web_insomnia
