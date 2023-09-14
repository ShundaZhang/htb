const antiCSRFMiddleware = (req, res, next) => {
    const referer = (req.headers.referer? new URL(req.headers.referer).host : req.headers.host);
    const origin = (req.headers.origin? new URL(req.headers.origin).host : null);
  
    if (req.headers.host === (origin || referer)) {
      next();
    } else {
      return res.status(403).json({ error: 'CSRF detected' });
    }
};

module.exports = antiCSRFMiddleware;