#!/bin/bash

# Secure entrypoint
chmod 600 /entrypoint.sh
mkdir /tmp/mongodb

# Start mongodb
mongod --noauth --dbpath /tmp/mongodb/ &

# Wait for mongodb
until nc -z localhost 27017; do echo "not up" && sleep 1; done

# Populate mongodb
mongosh heros --eval "db.createCollection('users')"
mongosh heros --eval 'db.users.insert( { username: "admin", password: "HTB{f4k3_fl4g_f0r_t3st1ng}"} )'

# Run services
/usr/bin/supervisord -c /etc/supervisord.conf
