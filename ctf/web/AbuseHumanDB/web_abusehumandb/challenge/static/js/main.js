$(document).ready(() => {
	$('#submitBtn').on('click', submitURL);
	$('#urlText').keypress(() => $('#resp-msg').hide());
});

const loading = (state) => {
	$("#submitBtn").prop('disabled', state);
	if (state == true) {
		scrollToBottom();
		$('#loading-container').show();
		$('#progressbar').css({
			"width": "0%",
			"transition": "none"
		});
		setTimeout(() => {
			$('#progressbar').css({
				"width": "100%",
				"transition": "10s"
			});
		}, 100);
		$('#resp-msg').text('');
	} else {
		$('#loading-container').hide();
	}
}

const scrollToBottom = () => {
	$("html, body").animate({
		scrollTop: $(document).height()
	}, 1000);
}

const submitURL = async () => {
	loading(true);
	const card = $('#resp-msg');
	const url = $('#urlText').val();
	if ($.trim(url) === '') {
		card.text('Please input a valid URL first!');
		card.show();
		loading(false);
		return;
	}
	await fetch(`/api/entries`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				url: url
			}),
		})
		.then((response) => response.json()
			.then((resp) => {
				card.text(resp.message);
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.show();
		});
	loading(false);
}