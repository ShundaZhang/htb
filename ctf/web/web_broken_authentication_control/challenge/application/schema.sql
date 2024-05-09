DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `todos`;

CREATE TABLE `users` (
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`secret` TEXT NOT NULL
);

INSERT INTO `users` (`name`, `secret`) VALUES
	('admin', '%s');

CREATE TABLE `todos` (
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`done` INTEGER NOT NULL,
	`assignee` TEXT NOT NULL
);

INSERT INTO `todos` (`name`, `done`, `assignee`) VALUES
	('HTB{f4k3_fl4g_f0r_t3st1ng}', 0, 'admin');