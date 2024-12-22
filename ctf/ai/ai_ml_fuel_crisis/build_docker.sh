docker rm -f misc_fuel_crisis
docker build -t misc_fuel_crisis . && \
docker run --name=misc_fuel_crisis --rm -p1337:1337 -it misc_fuel_crisis