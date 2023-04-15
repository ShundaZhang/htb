#!/bin/bash
docker build --tag=breaking_grad .
docker run -p 1337:1337 --rm --name=breaking_grad -it breaking_grad