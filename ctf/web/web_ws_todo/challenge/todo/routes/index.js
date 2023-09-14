const express = require('express');
const expressWs = require('@wll8/express-ws');
const crypto = require('crypto');

const { doReportHandler } = require('../util/report');
const { encrypt, decrypt } = require('../util/crypto');

let db;
let sessionParser;

const router = express.Router();

router.get('/', (req, res) => {
    return res.render('index.pug');
});

router.get('/login', (req, res) => {
    return res.render('login.pug');
});

router.post('/login', async (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    if (!username || !password) {
        return res.status(400).json({ error: 'Missing username or password' });
    }

    if (result = await db.loginUser(username, password)) {
        req.session.userId = result.id;
        return res.status(200).json({ success: 'User logged in' });
    } else {
        return res.status(400).json({ error: 'Invalid username or password' });
    }
});

router.get('/register', (req, res) => {
    return res.render('register.pug');
});

router.post('/register', async (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    if (!username || !password) {
        return res.status(400).json({
            error: 'Missing username or password'
        });
    }

    if (password.length < 8) {
        return res.status(400).json({
            error: 'Password must be at least 8 characters long'
        });
    }

    if (await db.userExists(username)) {
        return res.status(400).json({ error: 'User already exists' });
    } else {
        const secret = crypto.randomBytes(16).toString('hex');
        await db.registerUser(username, password, secret);
        return res.status(200).json({ success: 'User registered' });
    }

    return res.status(200).json({ success: true });
});

router.get('/secret', async (req, res) => {
    const result = await db.getSecret(req.session.userId);
    if (result) {
        return res.status(200).json({ secret: result });
    }
    return res.status(400).json({ error: 'No secret found' });
});

router.post('/decrypt', async (req, res) => {
    if (!req.body.secret) {
        return res.status(400).json({ error: 'Missing secret' });
    }

    if (!req.body.cipher) {
        return res.status(400).json({ error: 'Missing cipher' });
    }

    try {
        const result = decrypt(req.body.cipher, req.body.secret);
        return res.status(200).json({ decrypted: result });
    } catch (e) {
        return res.status(400).json({ error: 'Invalid key or cipher' });
    }
});

// Report any suspicious activity to the admin!
router.post('/report', doReportHandler);

module.exports = (database, session) => {
    db = database;
    sessionParser = session;
    return router;
};