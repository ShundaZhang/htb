#!/bin/bash

# Initialize SQLite database with a table and an initial user
touch /var/www/html/Insomnia/database/insomnia.db
chmod 666 /var/www/html/Insomnia/database/insomnia.db

sqlite3 /var/www/html/Insomnia/database/insomnia.db <<'EOF'
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
INSERT INTO users (username, password) VALUES ('administrator', LOWER(hex(randomblob(16))));
EOF

# Create JWT secret key
echo "JWT_SECRET='$(openssl rand -hex 32)'" >> /var/www/html/Insomnia/.env

# Start Apache server
apache2-foreground
