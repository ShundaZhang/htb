const { encrypt, decrypt } = require('./util/crypto');

let db;
let sessionParser;

const quotes = [
    "Genius is one percent inspiration and ninety-nine percent perspiration.",
    "Fate is in your hands and no one elses.",
    "Trust yourself. You know more than you think you do."
];

const wsHandler = (ws, req) => {
    let userId;
    sessionParser(req, {}, () => {
        if (req.session.userId) {
            userId = req.session.userId;
        } else {
            ws.close();
        }
    });

    ws.on('message', async (msg) => {
        const data = JSON.parse(msg);
        const secret = await db.getSecret(req.session.userId);

        if (data.action === 'add') {
            try {
                await db.addTask(userId, `{"title":"${data.title}","description":"${data.description}","secret":"${secret}"}`);
                ws.send(JSON.stringify({ success: true, action: 'add' }));
            } catch (e) {
                ws.send(JSON.stringify({ success: false, action: 'add' }));
            }
        }
        else if (data.action === 'get') {
            try {
                const results = await db.getTasks(userId);
                const tasks = [];
                for (const result of results) {

                    let quote;

                    if (userId === 1) {
                        quote = `A wise man once said, "the flag is ${process.env.FLAG}".`;
                    } else {
                        quote = quotes[Math.floor(Math.random() * quotes.length)];
                    }

                    try {
                        const task = JSON.parse(result.data);
                        tasks.push({
                            title: encrypt(task.title, task.secret),
                            description: encrypt(task.description, task.secret),
                            quote: encrypt(quote, task.secret)
                        });
                    } catch (e) {
                        console.log(`Error parsing task ${result.data}: ${e}`);
                    }
                }
                ws.send(JSON.stringify({ success: true, action: 'get', tasks: tasks }));
            } catch (e) {
                ws.send(JSON.stringify({ success: false, action: 'get' }));
            }
        }
        else {
            ws.send(JSON.stringify({ success: false, error: 'Invalid action' }));
        }
    });
};

module.exports = (database, session) => {
    db = database;
    sessionParser = session;
    return wsHandler;
};