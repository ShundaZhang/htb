#!/bin/sh

set -e

DB_PATH="/www/app/database.db"

if [ ! -f "$DB_PATH" ]; then
    sqlite3 "$DB_PATH" <<- 'EOF'
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        api_key TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
EOF
fi

RANDOM_PASSWORD=$(openssl rand -base64 16 | tr -d '\n') && export RANDOM_PASSWORD

sqlite3 "$DB_PATH" <<- EOF
    INSERT INTO users (username, password, email, api_key)
    VALUES ('admin', '$RANDOM_PASSWORD', 'admin@hackthebox.com', 'HTB{f4k3_fl4g_f0r_t35t1ng}');
EOF

mkdir -p /var/cache/nginx \
    && mkdir -p /var/log/gunicorn  \
    && chown -R nobody:nogroup /var/log/gunicorn \
    && chown -R nobody:nogroup /www 

nginx -g 'daemon off;' &
exec su nobody -s /bin/sh -c \
    "gunicorn \
    --bind 'unix:/tmp/gunicorn.sock' \
    --workers '2' \
    --access-logfile '/var/log/gunicorn/access.log' \
    wsgi:app"


