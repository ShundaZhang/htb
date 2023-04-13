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
            DROP TABLE IF EXISTS userData;

            CREATE TABLE IF NOT EXISTS userData (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username   VARCHAR(255) NOT NULL UNIQUE,
                balance    DOUBLE NOT NULL,
                coupons   VARCHAR(255) NOT NULL
            );

            DROP TABLE IF EXISTS products;

            CREATE TABLE IF NOT EXISTS products (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                item_name   VARCHAR(255) NOT NULL,
                price   DOUBLE NOT NULL
            );

            INSERT INTO products (item_name, price) VALUES ("A1", 0.55);
            INSERT INTO products (item_name, price) VALUES ("A2", 0.35);
            INSERT INTO products (item_name, price) VALUES ("A3", 0.25);
            INSERT INTO products (item_name, price) VALUES ("B4", 0.45);
            INSERT INTO products (item_name, price) VALUES ("B5", 0.15);
            INSERT INTO products (item_name, price) VALUES ("B6", 0.80);
            INSERT INTO products (item_name, price) VALUES ("C7", 0.35);
            INSERT INTO products (item_name, price) VALUES ("C8", 13.37);
            INSERT INTO products (item_name, price) VALUES ("C9", 0.69);

            DROP TABLE IF EXISTS coupons;

            CREATE TABLE IF NOT EXISTS coupons (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                coupon_code   VARCHAR(255) NOT NULL,
                value   DOUBLE NOT NULL
            );

            INSERT INTO coupons (coupon_code, value) VALUES ("HTB_100", 1.00);
        `);
	}

	async registerUser(username) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('INSERT INTO userData (username, balance, coupons) VALUES ( ?, 0.00,  "")');
				resolve((await stmt.run(username)));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getUser(user) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM userData WHERE username = ?');
				resolve(await stmt.get(user));
			} catch(e) {
				reject(e);
			}
		});
	}

	async setBalance(username, balance) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('UPDATE userData SET balance = ? WHERE username = ?');
				resolve(await stmt.get(balance, username));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getProduct(item) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM products where item_name = ?;');
				resolve(await stmt.get(item));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getCoupons() {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM coupons;');
				resolve(await stmt.all());
			} catch(e) {
				reject(e);
			}
		});
	}

	async getCouponValue(coupon_code) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT value FROM coupons WHERE coupon_code=?;');
				resolve(await stmt.get(coupon_code));
			} catch(e) {
				reject(e);
			}
		});
	}

	async addBalance(user, coupon_value) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('UPDATE userData SET balance = balance + ? WHERE username = ?');
				resolve((await stmt.run(coupon_value, user)));
			} catch(e) {
				reject(e);
			}
		});
	}

	async setCoupon(user, coupon_code) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('UPDATE userData SET coupons = coupons || ? WHERE username = ?');
				resolve((await stmt.run(coupon_code, user)));
			} catch(e) {
				reject(e);
			}
		});
	}

}

module.exports = Database;