#!/bin/bash
docker build --tag=magic .
docker run -p 1337:1337 --rm --name=magic magic