const fs             = require('fs');
const bot            = require('../bot');
const path           = require('path');
const express        = require('express');
const router         = express.Router();
const JWTHelper      = require('../helpers/JWTHelper');
const UploadHelper   = require('../helpers/UploadHelper')
const AuthMiddleware = require('../middleware/AuthMiddleware');


let db;

const response = data => ({ message: data });

router.get('/', (req, res) => {
	return res.render('index.html');
});

router.post('/api/register', async (req, res) => {
	const { username, password } = req.body;

	if (username && password) {
		return db.checkUser(username)
			.then(user => {
				if (user) return res.status(401).send(response('User already registered!'));
				return db.registerUser(username, password)
					.then(()  => res.send(response('User registered successfully!')))
			})
			.catch(() => res.send(response('Something went wrong!')));
	}
	return res.status(401).send(response('Please fill out all the required fields!'));
});

router.post('/api/login', async (req, res) => {
	const { username, password } = req.body;

	if (username && password) {
		return db.loginUser(username, password)
			.then(user => {
				let token = JWTHelper.sign({ username: user.username });
				res.cookie('session', token, { maxAge: 3600000 });
				return res.send(response('User authenticated successfully!'));
			})
			.catch(() => res.status(403).send(response('Invalid username or password!')));
	}
	return res.status(500).send(response('Missing parameters!'));
});

router.get('/feed', AuthMiddleware, async (req, res, next) => {
	return db.getUser(req.data.username)
		.then(user => {
			if(user === undefined) return res.redirect('/');
			return db.getPosts()
				.then(feed => {
					res.render('feed.html', { feed });
				})
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/profile', AuthMiddleware, async (req, res, next) => {
	return db.getUser(req.data.username)
		.then(user => {
			if(user === undefined) return res.redirect('/');
			res.render('profile.html', { user });
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/review', async (req, res, next) => {
	if(req.ip != '127.0.0.1') return res.redirect('/');

	return db.getPosts(0)
		.then(feed => {
			res.render('review.html', { feed });
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.post('/api/submit', AuthMiddleware, async (req, res) => {
	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/'); 
			const { content } = req.body;
			if(content){
				twoDots = content.match(/\./g);
				if(twoDots == null || twoDots.length != 2){
					return res.status(403).send(response('Your story must contain two sentences! We call it TwoDots Horror!'));
				}
				return db.addPost(user.username, content)
					.then(() => {
						bot.purgeData(db);
						res.send(response('Your submission is awaiting approval by Admin!'));
					});
			}
			return res.status(403).send(response('Please write your story first!'));
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.post('/api/upload', AuthMiddleware, async (req, res) => {
	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/');
			if (!req.files) return res.status(400).send(response('No files were uploaded.'));
			return UploadHelper.uploadImage(req.files.avatarFile)
				.then(filename => {
					return db.updateAvatar(user.username,filename)
						.then(()  => {
							res.send(response('Image uploaded successfully!'));
							if(user.avatar != 'default.jpg') 
								fs.unlinkSync(path.join(__dirname, '/../uploads',user.avatar)); // remove old avatar
						})
				})
		})
		.catch(err => res.status(500).send(response(err.message)));
});

router.get('/api/avatar/:username', async (req, res) => {
	return db.getUser(req.params.username)
		.then(user => {
			if (user === undefined) return res.status(404).send(response('user does not exist!'));
			avatar = path.join(__dirname, '/../uploads', user.avatar);
			return res.sendFile(avatar);
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/logout', (req, res) => {
	res.clearCookie('session');
	return res.redirect('/');
});

module.exports = database => { 
	db = database;
	return router;
};