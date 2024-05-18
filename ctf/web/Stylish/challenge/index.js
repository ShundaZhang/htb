const express       = require('express');
const app           = express();
const path          = require('path');
const nunjucks      = require('nunjucks');
const routes        = require('./routes');
const Database      = require('./database');
const TokenHelper   = require('./helpers/TokenHelper')

const db = new Database('web-stylish.db');

app.use(express.json())

app.use(function(req, res, next) {
	res.setHeader("Content-Security-Policy", "default-src 'self'; object-src 'none'; img-src 'self'; style-src 'self'; font-src 'self' *;")
    next();
});

nunjucks.configure('views', {
	autoescape: true,
	express: app
});

app.set('views', './views');
app.use('/assets', express.static(path.resolve('assets')));
app.use('/card_styles', express.static(path.resolve('card_styles')));

app.use(routes(db));

app.disable('etag');

app.all('*', (req, res) => {
    return res.status(404).send({
        message: '404 page not found'
    });
});

(async () => {
    await db.connect();
    await db.migrate();

    // Token will not contains any repeated characters
    process.env.approvalToken = TokenHelper.generateToken();
    process.env.rejectToken   = TokenHelper.generateToken();
        
    app.listen(1337, '0.0.0.0', () => console.log('Listening on port 1337'));
})();
