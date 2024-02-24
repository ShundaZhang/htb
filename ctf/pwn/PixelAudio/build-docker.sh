#!/bin/sh
docker build --tag=pixel_audio .
docker run -it -p 1337:1337 --rm --name=pixel_audio pixel_audio