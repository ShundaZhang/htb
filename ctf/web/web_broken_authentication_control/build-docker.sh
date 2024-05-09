#!/bin/bash
docker rm -f web_todo_or_not_todo
docker build --tag=web_todo_or_not_todo .
docker run -p 1337:1337 --restart=on-failure --name=web_todo_or_not_todo web_todo_or_not_todo