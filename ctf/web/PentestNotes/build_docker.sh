#!/bin/bash
docker rm -f web_pentestnote
docker build --no-cache --tag=web_pentestnote .
docker run -p 1337:8080 --rm --name=web_pentestnote -it web_pentestnote
