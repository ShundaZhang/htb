#!/bin/bash
docker rm -f web_abusehumandb
docker build -t web_abusehumandb .
docker run --name=web_abusehumandb --rm -p1337:1337 -it web_abusehumandb
