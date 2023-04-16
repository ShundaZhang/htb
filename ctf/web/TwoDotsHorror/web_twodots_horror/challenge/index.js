const express       = require('express');
const fileUpload    = require('express-fileupload');
const app           = express();
const path          = require('path');
const bodyParser    = require('body-parser');
const cookieParser  = require('cookie-parser');
const nunjucks      = require('nunjucks');
const routes        = require('./routes');
const Database      = require('./database');


const db = new Database('TwoDots-Horror.db');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

app.use(fileUpload({ limits: {
		fileSize: 2 * 1024 * 1024 // 2 MB
	},
	abortOnLimit: true
 }));

app.use(function(req, res, next) {
	res.setHeader("Content-Security-Policy", "default-src 'self'; object-src 'none'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com;")
	next();
});

nunjucks.configure('views', {
	autoescape: true,
	express: app
});

app.set('views', './views');
app.use('/static', express.static(path.resolve('static')));

app.use(routes(db));

app.all('*', (req, res) => {
	return res.status(404).send({
		message: '404 page not found'
	});
});

(async () => {
	await db.connect();
	await db.migrate();
	app.listen(1337, '0.0.0.0', () => console.log('Listening on port 1337'));
})();