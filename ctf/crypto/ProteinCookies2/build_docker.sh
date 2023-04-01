#!/bin/bash
docker rm -f crypto_protein_cookies
docker build -t crypto_protein_cookies . && \
docker run --name=crypto_protein_cookies --rm -p1337:1337 -it crypto_protein_cookies
