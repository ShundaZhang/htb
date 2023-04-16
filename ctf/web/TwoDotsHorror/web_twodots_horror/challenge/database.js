const sqlite = require('sqlite-async');

class Database {
	constructor(db_file) {
		this.db_file = db_file;
		this.db = undefined;
	}
	
	async connect() {
		this.db = await sqlite.open(this.db_file);
	}

	async migrate() {
		return this.db.exec(`
            DROP TABLE IF EXISTS users;

            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username   VARCHAR(255) NOT NULL UNIQUE,
                password   VARCHAR(255) NOT NULL,
                avatar     VARCHAR(255) NOT NULL
            );

            DROP TABLE IF EXISTS posts;

            CREATE TABLE IF NOT EXISTS posts (
                id         INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
                author  VARCHAR(255) NOT NULL,
                content    VARCHAR(255) NOT NULL,
                approved   INTEGER      NOT NULL,
                created_at TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
            );

            INSERT INTO posts (author, approved, content) VALUES ('ColonelAengus', 1, 'Our baby girl is finally crawling for the first time. I just wish it wasn’t on the ceiling.');
            INSERT INTO posts (author, approved, content) VALUES ('windowsXP', 1, 'Keyboard not responding. Press any key to continue.');
            INSERT INTO posts (author, approved, content) VALUES ('unkn0wn', 1, 'There was a picture in my phone of me sleeping. I live alone.');
            INSERT INTO posts (author, approved, content) VALUES ('Scry67', 1, 'The last man on Earth sat alone in a room. There was a knock at the door.');
            INSERT INTO posts (author, approved, content) VALUES ('fluffyponyza', 1, 'Day 312. Internet still not working.');
        `);
	}

	async registerUser(user, pass) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('INSERT INTO users (username, password, avatar) VALUES ( ?, ?, "default.jpg")');
				resolve((await stmt.run(user, pass)));
			} catch(e) {
				reject(e);
			}
		});
	}

	async loginUser(user, pass) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT username FROM users WHERE username = ? and password = ?');
				resolve(await stmt.get(user, pass));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getUser(user) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM users WHERE username = ?');
				resolve(await stmt.get(user));
			} catch(e) {
				reject(e);
			}
		});
	}

	async checkUser(user) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT username FROM users WHERE username = ?');
				let row = await stmt.get(user);
				resolve(row !== undefined);
			} catch(e) {
				reject(e);
			}
		});
	}

	async updateAvatar(user, avatar) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('UPDATE users SET avatar = ? WHERE username = ?');
				resolve(await stmt.run(avatar, user));
			} catch(e) {
				reject(e);
			}
		});
	}

	async addPost(author, content) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('INSERT INTO posts (author, content, approved) VALUES (? , ?, 0)');
				resolve(await stmt.run(author, content));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getPosts(approved=1) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM posts WHERE approved = ?');
				resolve(await stmt.all(approved));
			} catch(e) {
				reject(e);
			}
		});
	}
}

module.exports = Database;