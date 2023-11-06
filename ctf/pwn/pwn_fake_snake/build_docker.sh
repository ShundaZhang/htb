#!/bin/bash

docker build --tag=pwn_fake_snake . && \
    docker run --rm --name pwn_fake_snake -p 1337:1337 pwn_fake_snake
