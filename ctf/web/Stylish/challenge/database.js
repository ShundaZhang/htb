const sqlite = require('sqlite-async');
const crypto = require('crypto');

class Database {
    constructor(db_file) {
        this.db_file = db_file;
        this.db = undefined;
    }
    
    async connect() {
        this.db = await sqlite.open(this.db_file);
    }

    async migrate() {
        const flagTable = 'flag_' + crypto.randomBytes(4).toString('hex');

        return this.db.exec(`
            PRAGMA case_sensitive_like=ON; 
            
            DROP TABLE IF EXISTS submissions;
            CREATE TABLE IF NOT EXISTS submissions (
                id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                css         TEXT NOT NULL,
                approved    BOOLEAN NOT NULL 
            );

            DROP TABLE IF EXISTS comments;
            CREATE TABLE IF NOT EXISTS comments (
                id               INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_submission    INTEGER NOT NULL,
                content          TEXT NOT NULL
            );

            DROP TABLE IF EXISTS ${flagTable};
            CREATE TABLE IF NOT EXISTS ${flagTable} (
                flag          VARCHAR(255) NOT NULL
            );
            
            INSERT INTO ${flagTable} VALUES ('HTB{f4k3_fl4g_f0r_t3st1ng}');
        `);
    }

    async getSubmission(id) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare("SELECT * FROM submissions WHERE id = ?");
                resolve(await stmt.get(id));
            } catch(e) {
                reject(e);
            }
        });
    }

	async insertSubmission(css) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('INSERT INTO submissions (css, approved) VALUES (?, 0)');
                resolve((await stmt.run(css).then((result) => { return result.lastID; })));
			} catch(e) {
				reject(e);
			}
		});
	}
    
	async updateSubmissionStatus(id, approved) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('UPDATE submissions SET approved = ? WHERE id = ?');
				resolve(await stmt.run(approved, id));
			} catch(e) {
				reject(e);
			}
		});
	}

    async deleteSubmission(id) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('DELETE FROM submissions WHERE id = ?');
				resolve(await stmt.run(id));
			} catch(e) {
				reject(e);
			}
		});
	}

	async insertComment(submissionID, commentContent) {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('INSERT INTO comments (id_submission, content) VALUES (?, ?)');
                resolve((await stmt.run(submissionID, commentContent).then((result) => { return result.lastID; })));
			} catch(e) {
				reject(e);
			}
		});
	}

	async getSubmissionComments(submissionID, pagination=10) {
		return new Promise(async (resolve, reject) => {
			try {
                const stmt = `SELECT content FROM comments WHERE id_submission = ${submissionID} LIMIT ${pagination}`;
                resolve(await this.db.all(stmt));
			} catch(e) {
				reject(e);
			}
		});
	}
}

module.exports = Database;
