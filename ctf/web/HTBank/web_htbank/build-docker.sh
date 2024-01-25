#!/bin/bash
docker rm -f web_htbank
docker build --tag=web_htbank .
docker run -p 1337:1337 --rm --name=web_htbank web_htbank