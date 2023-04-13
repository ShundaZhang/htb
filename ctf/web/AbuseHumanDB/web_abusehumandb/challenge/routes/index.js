const bot             = require('../bot');
const path            = require('path');
const express         = require('express');
const router          = express.Router();

const response = data => ({ message: data });
const isLocalhost = req => ((req.ip == '127.0.0.1' && req.headers.host == '127.0.0.1:1337') ? 0 : 1);
let db;

router.get('/', (req, res) => {
	return res.sendFile(path.resolve('views/index.html'));
});

router.get('/entries', (req, res) => {
	return res.sendFile(path.resolve('views/entries.html'));
});

router.get('/api/entries', (req, res) => {
	return db.listEntries(isLocalhost(req))
		.then(entries => {
			res.json(entries);
		})
		.catch(() => res.send(response('Something went wrong!')));
});

router.post('/api/entries', (req, res) => {
	const { url } = req.body;
	if (url) {
		uregex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)/
		if (url.match(uregex)) {
			return bot.visitPage(url)
				.then(() => res.send(response('Your submission is now pending review!')))
				.catch(() => res.send(response('Something went wrong! Please try again!')))
		}
		return res.status(403).json(response('Please submit a valid URL!'));
	}
	return res.status(403).json(response('Missing required parameters!'));
});

router.get('/api/entries/search', (req, res) => {
	if(req.query.q) {
		const query = `${req.query.q}%`;
		return db.getEntry(query, isLocalhost(req))
			.then(entries => {
				if(entries.length == 0) return res.status(404).send(response('Your search did not yield any results!'));
				res.json(entries);
			})
			.catch(() => res.send(response('Something went wrong! Please try again!')));
	}
	return res.status(403).json(response('Missing required parameters!'));
});

module.exports = database => {
	db = database;
	return router;
};