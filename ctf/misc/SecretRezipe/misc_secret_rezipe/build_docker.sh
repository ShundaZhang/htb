#!/bin/bash

docker build -t secret-rezipe .
docker run -p 1337:1337 --rm --name=secret-rezipe -it secret-rezipe
