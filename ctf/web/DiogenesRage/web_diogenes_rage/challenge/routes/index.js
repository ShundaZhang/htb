const fs             = require('fs');
const express        = require('express');
const router         = express.Router();
const JWTHelper      = require('../helpers/JWTHelper');
const AuthMiddleware = require('../middleware/AuthMiddleware');

let db;

const response = data => ({ message: data });

router.get('/', (req, res) => {
	return res.render('index.html');
});

router.post('/api/purchase', AuthMiddleware, async (req, res) => {
	return db.getUser(req.data.username)
		.then(async user => {
			if (user === undefined) {
				await db.registerUser(req.data.username);
				user = { username: req.data.username, balance: 0.00, coupons: '' };
			}
			const { item } = req.body;
			if (item) {
				return db.getProduct(item)
					.then(product => {
						if (product == undefined) return res.send(response("Invalid item code supplied!"));
						if (product.price <= user.balance) {
							newBalance = parseFloat(user.balance - product.price).toFixed(2);
							return db.setBalance(req.data.username, newBalance)
								.then(() => {
									if (product.item_name == 'C8') return res.json({
										flag: fs.readFileSync('/app/flag').toString(),
										message: `Thank you for your order! $${newBalance} coupon credits left!`
									})
									res.send(response(`Thank you for your order! $${newBalance} coupon credits left!`))
								});
						}
						return res.status(403).send(response("Insufficient balance!"));

					})
			}
			return res.status(401).send(response('Missing required parameters!'));
		});
});

router.post('/api/coupons/apply', AuthMiddleware, async (req, res) => {
	return db.getUser(req.data.username)
		.then(async user => {
			if (user === undefined) {
				await db.registerUser(req.data.username);
				user = { username: req.data.username, balance: 0.00, coupons: '' };
			}
			const { coupon_code } = req.body;
			if (coupon_code) {
				if (user.coupons.includes(coupon_code)) {
					return res.status(401).send(response("This coupon is already redeemed!"));
				}
				return db.getCouponValue(coupon_code)
					.then(coupon => {
						if (coupon) {
							return db.addBalance(user.username, coupon.value)
								.then(() => {
									db.setCoupon(user.username, coupon_code)
										.then(() => res.send(response(`$${coupon.value} coupon redeemed successfully! Please select an item for order.`)))
								})
								.catch(() => res.send(response("Failed to redeem the coupon!")));
						}
						res.send(response("No such coupon exists!"));
					})
			}
			return res.status(401).send(response("Missing required parameters!"));
		});
});

router.get('/api/reset', async (req, res) => {
	res.clearCookie('session');
	res.send(response("Insert coins below!"));
});

module.exports = database => {
	db = database;
	return router;
};