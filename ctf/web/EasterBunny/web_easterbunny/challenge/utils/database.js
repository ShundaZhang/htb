const sqlite = require("sqlite-async");

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
            DROP TABLE IF EXISTS messages;

            CREATE TABLE IF NOT EXISTS messages (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                message   VARCHAR(300) NOT NULL,
                hidden    INTEGER NOT NULL
            );

            INSERT INTO messages (id, message, hidden) VALUES
              (1, "Dear Easter Bunny,\nPlease could I have the biggest easter egg you have?\n\nThank you\nGeorge", 0),
              (2, "Dear Easter Bunny,\nCould I have 3 chocolate bars and 2 easter eggs please!\nYours sincerly, Katie", 0),
              (3, "Dear Easter Bunny, Santa's better than you! HTB{f4k3_fl4g_f0r_t3st1ng}", 1),
              (4, "Hello Easter Bunny,\n\nCan I have a PlayStation 5 and a chocolate chick??", 0),
              (5, "Dear Ester Bunny,\nOne chocolate and marshmallow bunny please\n\nLove from Milly", 0),
              (6, "Dear Easter Bunny,\n\nHow are you? Im fine please may I have 31 chocolate bunnies\n\nThank you\nBeth", 0);
            `);
    }

    async getMessage(id) {
        return new Promise(async(resolve, reject) => {
            try {
                let stmt = await this.db.prepare("SELECT * FROM messages WHERE id = ?");
                resolve(await stmt.get(id));
            } catch (e) {
                reject(e);
            }
        });
    }

    async getMessageCount() {
        return new Promise(async(resolve, reject) => {
            try {
                let stmt = await this.db.prepare("SELECT COUNT(*) as count FROM messages");
                resolve(await stmt.get());
            } catch (e) {
                reject(e);
            }
        });
    }

    async insertMessage(message) {
        return new Promise(async(resolve, reject) => {
            try {
                let stmt = await this.db.prepare("INSERT INTO messages (message, hidden) VALUES (?, ?)");
                resolve(await stmt.run(message, false));
            } catch (e) {
                reject(e);
            }
        });
    }
}

module.exports = Database;