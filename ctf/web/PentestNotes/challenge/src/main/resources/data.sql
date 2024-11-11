CREATE TABLE notes (
                       id bigint auto_increment,
                       name varchar(50),
                       note nvarchar(200)
);
INSERT INTO notes (id, name,note) VALUES (1, 'SQL Injection', 'One  '' to rule them all');
INSERT INTO notes (id, name,note) VALUES (2, 'Cross Site Scripting', 'Script alert 1 !!!!!!!!!');
INSERT INTO notes (id, name,note) VALUES (3, 'Skill issue', 'IDK, can you tell me?                   ¯\_(ツ)_/¯');


CREATE TABLE users (
                       id bigint auto_increment,
                       username varchar(50),
                       password nvarchar(200)
);
INSERT INTO users (id, username,password) VALUES (1, 'user', '123');
