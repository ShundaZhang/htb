$(document).ready(() => {
    $('#postComment').on('click', postComment);
    $('#pagination').on('change', updateComments);
});

// Global variables
let responseBox = $('#responseMsg');
let submissionID = $('#commentContent').data("id");

const postComment = async (e) => {
    var btn = $(e.target);
    btn.prop('disabled', true);

	responseBox.attr('class', 'alert alert-info mt-3');
	responseBox.hide();
	
	let commentContent = $('#commentContent').val();
	if ($.trim(commentContent) === '') {
		btn.prop('disabled', false);
		responseBox.text('Comment field cannot be empty!');
		responseBox.attr('class', 'alert alert-danger mt-3');
		responseBox.show();
		return;
	}

	await fetch('/api/comment/submit', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({submissionID: submissionID, commentContent: commentContent}),
		})
		.then((response) => response.json()
			.then((resp) => {
				responseBox.attr('class', 'alert alert-danger mt-3');
				if (response.status == 200) {
					responseBox.attr('class', 'alert alert-success mt-3');
				}
				responseBox.text(resp.message);
				responseBox.show();

				updateComments();
			}))
		.catch((error) => {
			responseBox.text(error);
			responseBox.attr('class', 'alert alert-danger mt-3');
			responseBox.show();
		});

        btn.prop('disabled', false);
}

const updateComments = async (e) => {
	let pagination = $('#pagination').find('option:selected').val();

	fetch('/api/comment/entries', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({submissionID: submissionID, pagination: pagination}),
	})
	.then((response) => response.json()
		.then((resp) => {
			if (response.status == 200) {
				let commentsBox = $('#comments');
				commentsBox.empty();

				$.each(resp, function( index, comment ) {
					commentsBox.append('<div>' + comment.content + '</div>');
				});
			}
		}))
	.catch((error) => {
		responseBox.text(error);
		responseBox.attr('class', 'alert alert-danger mt-3');
		responseBox.show();
	});	
}
