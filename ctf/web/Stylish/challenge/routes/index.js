const bot             = require('../bot');
const path            = require('path');
const express         = require('express');
const fs              = require('fs');
const router          = express.Router();

const response = data => ({ message: data });
const isAdmin = req => ((req.ip == '127.0.0.1') ? 1 : 0);

let db;

router.get('/', (req, res) => {
	return res.sendFile(path.resolve('views/submit.html'));
});

router.get('/view/:id', (req, res) => {
    return db.getSubmission(req.params.id)
        .then(submission => {
            if (submission === undefined) return res.status(404).send(response('Submission does not exist!'));

            const cssFile = `/card_styles/${req.params.id}.css`;
            
            if(submission.approved == 0) {
                // Only admin can view unaccepted submissions
                if(isAdmin(req) == 0)
                    return res.status(403).send(response('This submission has not been reviewed yet'));
                    
                const approvalToken = process.env.approvalToken;        
                const rejectToken = process.env.rejectToken;        
    
                return res.render(path.resolve('views/card_unapproved.html'), {
                    cssFile: cssFile,
                    approvalToken: approvalToken,
                    rejectToken: rejectToken,
                    submissionID: submission.id
                });
            }
            else {
                return db.getSubmissionComments(submission.id)
				.then(comments => {
                    return res.render(path.resolve('views/card_approved.html'), {
                        cssFile: cssFile,
                        submissionID: submission.id,
                        comments: comments
                    });
				})
            }
        })
        .catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/approve/:id/:approvalToken', (req, res) => {
    if(isAdmin(req) == 0)
        return res.status(403).send(response('Only admin can access this function!'));
    
    return db.getSubmission(req.params.id)
        .then(submission => {
            if (submission === undefined) return res.status(404).send(response('Submission does not exist!'));

            if(process.env.approvalToken == req.params.approvalToken) {
                return db.updateSubmissionStatus(submission.id, 1)
                    .then(()  => {
                        return res.send(response('Submission has been approved!'));
                    })
            }
            else {
                return res.status(403).send(response('Token doesn\'t match!'));
            }
        })
        .catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/reject/:id/:rejectToken', (req, res) => {
    if(isAdmin(req) == 0)
        return res.status(403).send(response('Only admin can access this function!'));
        
    return db.getSubmission(req.params.id)
        .then(submission => {
            if (submission === undefined) return res.status(404).send(response('Submission does not exist!'));

            if(process.env.rejectToken == req.params.rejectToken) {
                return db.deleteSubmission(submission.id, 1)
                    .then(()  => {
                        fs.unlinkSync(`card_styles/${submission.id}.css`);
                        return res.send(response('Submission has been deleted!'));
                    })
            }
            else {
                return res.status(403).send(response('Token doesn\'t match!'));
            }
        })
        .catch(() => res.status(500).send(response('Something went wrong!')));
});

router.post('/api/submission/submit', async (req, res) => {
    const { customCSS } = req.body;

    if(customCSS) {
        return db.insertSubmission(customCSS)
            .then(submissionID => {
                fs.writeFile(`card_styles/${submissionID}.css`, customCSS, function (err) {
                    if (err) return console.log(err);
                });
                bot.visitURL(`http://127.0.0.1:1337/view/${submissionID}`);
                
                return res.send(response(
                    `Your submission (Number ${submissionID}) successfully sent!<br>When approved it will become available <a href="/view/${submissionID}">here</a>`
                ));
            });
    }
    return res.status(403).send(response('CSS code field cannot be empty!'));
});

router.post('/api/comment/submit', async (req, res) => {
    const { submissionID, commentContent } = req.body;

    if(submissionID && commentContent) {
        return db.getSubmission(submissionID)
        .then(submission => {
            if (submission === undefined) return res.status(404).send(response('Submission does not exist!'));

            if(submission.approved == 0)
                return res.status(403).send(response('This submission has not been reviewed yet'));

            return db.insertComment(submissionID, commentContent)
            .then(commentID => {
                return res.send(response('Your comment was successfully sent!'));
            });
        })
        .catch(() => res.status(500).send(response('Something went wrong!')));
    }
    return res.status(403).send(response('Comment field and submission ID should be provided!'));
});

router.post('/api/comment/entries', async (req, res) => {
    const { submissionID, pagination } = req.body;

    if(submissionID && pagination) {
        return db.getSubmission(submissionID)
        .then(submission => {
            if (submission === undefined) return res.status(404).send(response('Submission does not exist!'));
            
            if(submission.approved == 0)
                return res.status(403).send(response('This submission has not been reviewed yet'));

                return db.getSubmissionComments(submissionID, pagination)
				.then(comments => {
					res.send(comments);
				})
        })
        .catch(() => res.status(500).send(response('Something went wrong!')));
    }
});

module.exports = database => {
	db = database;
	return router;
};
