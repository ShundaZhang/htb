$(document).ready(function() {

	// attach event
	$("#submit-btn").on('click', addSubmission);
	$("#content-box").on('keydown', function() {
		$("#resp").text('Submit Your Story')
	});

});


async function addSubmission() {

	$("#submit-btn").prop("disabled", true); // disable multiple submission

	// prepare alert
	let card = $("#resp");

	// validate
	let content = $("#content-box").val();

	if ($.trim(content) === '') {
		$("#submit-btn").prop("disabled", false);
		card.text("Please type in your story first!");

		return;
	}

	const data = {
		content: content
	};

	await fetch('/api/submit', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json())
		.then((resp) => {
			card.text(resp.message);
		})
		.catch((error) => {
			card.text(error);
		});

	$("#submit-btn").prop("disabled", false);
}