docker build -t secure_server .
docker run  --name=secure_server --rm -p 80:80 -p 445:445 -it secure_server
