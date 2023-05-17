#!/bin/sh

docker build . -t pwn_arms_roped
docker run --rm --name pwn_arms_roped -it -p1337:1337 pwn_arms_roped
