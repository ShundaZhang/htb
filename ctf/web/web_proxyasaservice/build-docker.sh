#!/bin/bash
docker rm -f web_proxyasaservice
docker build --tag=web_proxyasaservice .
docker run -p 1337:1337 -it --rm --name=web_proxyasaservice web_proxyasaservice