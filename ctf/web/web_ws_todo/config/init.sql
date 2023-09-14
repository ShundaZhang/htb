ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'REDACTED';
CREATE USER 'web'@'localhost' IDENTIFIED WITH mysql_native_password BY 'REDACTED';
FLUSH PRIVILEGES;

CREATE DATABASE todo;
USE todo;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    secret VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE todos (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    data VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (username, password, secret) VALUES ('admin', 'REDACTED', 'REDACTED');

GRANT INSERT, SELECT ON todo.users TO 'web'@'localhost';
GRANT INSERT, SELECT ON todo.todos TO 'web'@'localhost';
FLUSH PRIVILEGES;