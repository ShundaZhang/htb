const authSecret = require('crypto').randomBytes(69).toString('hex');

const isAdmin = (req, res) => {
  return req.ip === '127.0.0.1' && req.cookies['auth'] === authSecret;
};

module.exports = {
  authSecret,
  isAdmin,
};
