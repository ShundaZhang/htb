#!/bin/bash

docker build --tag=misc_shiny_hunter .
docker run -it -p 1337:1337 --rm --name=misc_shiny_hunter misc_shiny_hunter