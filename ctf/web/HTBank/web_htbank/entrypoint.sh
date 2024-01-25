#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo 'not up' && sleep .2; done

mysql -u root << EOF
DROP DATABASE if exists web_htbank;
CREATE DATABASE web_htbank;
CREATE TABLE web_htbank.users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    balance INTEGER NOT NULL DEFAULT 0,
    wallet_address VARCHAR(255) NOT NULL
);

CREATE TABLE web_htbank.flag (
    flag VARCHAR(255) NOT NULL,
    show_flag INTEGER NOT NULL
);

INSERT INTO web_htbank.flag(flag, show_flag) VALUES('HTB{FAKE_FLAG_FOR_TESTING}', 0);

CREATE USER 'xclow3n'@'localhost' IDENTIFIED BY 'xCl0w3n1337!!';
GRANT SELECT, INSERT, UPDATE ON web_htbank.* TO 'xclow3n'@'localhost';
FLUSH PRIVILEGES;
EOF

/usr/bin/supervisord -c /etc/supervisord.conf
