#!/bin/bash
docker rm -f ancient_interface
export DOCKER_BUILDKIT=1
docker build --tag=ancient_interface .
docker run -p 1337:5000 --restart=on-failure --name=ancient_interface ancient_interface
