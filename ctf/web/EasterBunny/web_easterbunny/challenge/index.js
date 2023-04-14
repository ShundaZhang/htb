const express      = require('express');
const app          = express();
const nunjucks     = require('nunjucks');
const cookieParser = require('cookie-parser');
const routes       = require('./routes/routes');
const Database     = require('./utils/database');

const db = new Database('./database.db');

app.use(cookieParser());
app.use(express.json());
app.set('trust proxy', process.env.PROXY !== 'false');
app.use('/static', express.static('static'));

nunjucks.configure("views", {
    autoescape: true,
    express: app,
    views: "templates",
});

app.use(routes(db));

app.all('*', (req, res) => {
    return res.status(404).send({
        message: '404 page not found'
    });
});

app.use(function (err, req, res, next) {
    res.status(500).json({
        message: 'Something went wrong!'
    });
});

(async() => {
    await db.connect();
    await db.migrate();
    app.listen(1337, '0.0.0.0', () => console.log('Listening on port 1337'));
})();