const util = require('util');
const mysql = require('mysql');

class Database {
    constructor(user, password, database) {
        this.db = mysql.createConnection({
            host: 'localhost',
            user: user,
            password: password,
            database: database,
            stringifyObjects: true
        });
        this.query = util.promisify(this.db.query).bind(this.db);
    }

    connect() {
        this.db.connect();
    }

    async userExists(username) {
        const result = await this.query('SELECT * FROM users WHERE username = ?', [username]);
        return result.length === 1;
    }

    async registerUser(username, password, secret) {
        const result = await this.query('INSERT INTO users (username, password, secret) VALUES (?, ?, ?)', [username, password, secret]);
        return result;
    }

    async loginUser(username, password) {
        const result = await this.query('SELECT * FROM users WHERE username = ? AND password = ?', [username, password]);
        return result.length === 1 ? result[0] : false;
    }

    async addTask(userId, data) {
        const result = await this.query('INSERT INTO todos (user_id, data) VALUES (?, ?)', [userId, data]);
        return result;
    }

    async getTasks(userId) {
        const result = await this.query('SELECT * FROM todos WHERE user_id = ?', [userId]);
        return result;
    }

    async getSecret(userId) {
        const result = await this.query('SELECT secret FROM users WHERE id = ?', [userId]);
        return result.length === 1 ? result[0].secret : false;
    }
}

module.exports = Database;