#!/bin/sh

DB_PATH="/opt/www/app/nothreshold.db"

sqlite3 "$DB_PATH" <<EOF
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', '$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32)');

.quit
EOF

uwsgi --ini /opt/www/app/uwsgi.ini &

haproxy -f /etc/haproxy/haproxy.cfg 

tail -f /dev/null

