const pug = require('pug');
const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const expressWs = require('@wll8/express-ws')

const routes = require('./routes');
const wsHandler = require('./wsHandler');
const Database = require('./database');
const authenticationMiddleware = require('./middleware/authenticationMiddleware');
const antiCSRFMiddleware = require('./middleware/antiCSRFMiddleware');

const db = new Database(process.env.MYSQL_USER, process.env.MYSQL_PASSWORD, 'todo');
db.connect();

const { app, wsRoute } = expressWs(express());

const sessionParser = session({
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true
})

app.use(sessionParser);
app.use(bodyParser.json());

app.use('/static', express.static('static'));
app.set('view engine', 'pug');

app.use(authenticationMiddleware);
app.use(antiCSRFMiddleware);
app.use(routes(db, sessionParser));
app.ws('/ws', wsHandler(db, sessionParser));

app.all('*', (req, res) => {
    return res.status(404).send({
        message: '404 page not found'
    });
});

app.listen(80, () => console.log('Listening on port 80'));