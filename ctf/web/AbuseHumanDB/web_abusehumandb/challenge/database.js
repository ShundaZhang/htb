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
            PRAGMA case_sensitive_like=ON; 

            DROP TABLE IF EXISTS userEntries;

            CREATE TABLE IF NOT EXISTS userEntries (
                id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title       VARCHAR(255) NOT NULL UNIQUE,
                url         VARCHAR(255) NOT NULL,
                approved    BOOLEAN NOT NULL
            );

            INSERT INTO userEntries (title, url, approved) VALUES ("Back The Hox :: Cyber Catastrophe Propaganda CTF against Aliens", "https://ctf.backthehox.ew/ctf/82", 1);
            INSERT INTO userEntries (title, url, approved) VALUES ("Drunk Alien Song | Patlamaya Devam (official video)", "https://www.youtune.com/watch?v=jPPT7TcFmAk", 1);
            INSERT INTO userEntries (title, url, approved) VALUES ("Mars Attacks! Earth is invaded by Martians with unbeatable weapons and a cruel sense of humor.", "https://www.imbd.com/title/tt0116996/", 1);
            INSERT INTO userEntries (title, url, approved) VALUES ("Professor Steven Rolling fears aliens could ‘plunder, conquer and colonise’ Earth if we contact them", "https://www.thebun.co.uk/tech/4119382/professor-steven-rolling-fears-aliens-could-plunder-conquer-and-colonise-earth-if-we-contact-them/", 1);
            INSERT INTO userEntries (title, url, approved) VALUES ("HTB{f4k3_fl4g_f0r_t3st1ng}","https://app.backthehox.ew/users/107", 0);
        `);
    }

    async listEntries(approved=1) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare("SELECT * FROM userEntries WHERE approved = ?");
                resolve(await stmt.all(approved));
            } catch(e) {
                console.log(e);
                reject(e);
            }
        });
    }

    async getEntry(query, approved=1) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare("SELECT * FROM userEntries WHERE title LIKE ? AND approved = ?");
                resolve(await stmt.all(query, approved));
            } catch(e) {
                console.log(e);
                reject(e);
            }
        });
    }

}

module.exports = Database;