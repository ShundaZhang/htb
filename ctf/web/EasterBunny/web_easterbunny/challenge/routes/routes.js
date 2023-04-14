const { isAdmin, authSecret } = require("../utils/authorisation");
const express                 = require("express");
const router                  = express.Router({caseSensitive: true});
const visit                   = require("../utils/bot.js");

let db;
let botVisiting = false;

const response = data => ({ message: data });

router.get("/", (req, res) => {
    return res.render("index.html", {
        cdn: `${req.protocol}://${req.hostname}:${req.headers["x-forwarded-port"] ?? 80}/static/`,
    });
});

router.get("/letters", (req, res) => {
    return res.render("viewletters.html", {
        cdn: `${req.protocol}://${req.hostname}:${req.headers["x-forwarded-port"] ?? 80}/static/`,
    });
});

router.post("/submit", async (req, res) => {
    const { message } = req.body;

    if (message) {
        return db.insertMessage(message)
            .then(async inserted => {
                try {
                    botVisiting = true;
                    await visit(`http://127.0.0.1/letters?id=${inserted.lastID}`, authSecret);
                    botVisiting = false;
                }
                catch (e) {
                    console.log(e);
                    botVisiting = false;
                }
                res.status(201).send(response(inserted.lastID));
            })
            .catch(() => {
                res.status(500).send(response('Something went wrong!'));
            });
    }
    return res.status(401).send(response('Missing required parameters!'));
});

router.get("/message/:id", async (req, res) => {
    try {
        const { id } = req.params;
        const { count } = await db.getMessageCount();
        const message = await db.getMessage(id);

        if (!message) return res.status(404).send({
            error: "Can't find this note!",
            count: count
        });

        if (message.hidden && !isAdmin(req))
            return res.status(401).send({
                error: "Sorry, this letter has been hidden by the easter bunny's helpers!",
                count: count
            });

        if (message.hidden) res.set("Cache-Control", "private, max-age=0, s-maxage=0 ,no-cache, no-store");

        return res.status(200).send({
            message: message.message,
            count: count,
        });
    } catch (error) {
        console.error(error);
        res.status(500).send({
            error: "Something went wrong!",
        });
    }
});

module.exports = (database) => {
    db = database;
    return router;
};