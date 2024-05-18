$(document).ready(() => {
    $('#submitBtn').on('click', submit);
});

const submit = async (e) => {
    var btn = $(e.target);
    btn.prop('disabled', true);

	let responseBox = $('#responseMsg');
	responseBox.attr('class', 'alert alert-info mt-3');
	responseBox.hide();

	let customCSS = $('#customCSS').val();
	if ($.trim(customCSS) === '') {
		btn.prop('disabled', false);
		responseBox.text('CSS code field cannot be empty!');
		responseBox.attr('class', 'alert alert-danger mt-3');
		responseBox.show();
		return;
	}

	await fetch('/api/submission/submit', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({customCSS: customCSS}),
		})
		.then((response) => response.json()
			.then((resp) => {
				responseBox.attr('class', 'alert alert-danger mt-3');
				if (response.status == 200) {
					responseBox.attr('class', 'alert alert-success mt-3');
				}
				responseBox.html(resp.message);
				responseBox.show();
			}))
		.catch((error) => {
			responseBox.text(error);
			responseBox.attr('class', 'alert alert-danger mt-3');
			responseBox.show();
		});

        btn.prop('disabled', false);
}
