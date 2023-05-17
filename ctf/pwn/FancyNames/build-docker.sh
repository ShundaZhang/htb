#!/bin/bash
docker build --tag=fancy_names .
docker run -p 1337:1337 --rm --name=fancy_names fancy_names