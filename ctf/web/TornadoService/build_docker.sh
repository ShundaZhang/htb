#!/bin/bash
docker rm -f web_tornado_service
docker build --tag=web_tornado_service .
docker run -p 1337:1337 --rm --name=web_tornado_service -it web_tornado_service