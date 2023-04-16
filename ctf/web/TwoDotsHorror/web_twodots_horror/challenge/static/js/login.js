// register enterKey event
(function($) {
	$.fn.catchEnter = function(sel) {
		return this.each(function() {
			$(this).on('keyup', sel, function(e) {
				if (e.keyCode == 13)
					$(this).trigger("enterkey");
			})
		});
	};
})(jQuery);


$(document).ready(function() {

	// set input events
	$("#login-btn").on('click', function() {
		auth('login')
	});
	$("#register-btn").on('click', function() {
		auth('register')
	});
	$("#username").catchEnter().on('enterkey', function() {
		auth('login')
	});
	$("#password").catchEnter().on('enterkey', function() {
		auth('login')
	});

});

function toggleInputs(state) {
	$("#username").prop("disabled", state);
	$("#password").prop("disabled", state);
	$("#login-btn").prop("disabled", state);
	$("#register-btn").prop("disabled", state);
}


async function auth(intent) {

	toggleInputs(true); // disable inputs
	console.log(intent);

	// prepare alert
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.hide();

	// validate
	let user = $("#username").val();
	let pass = $("#password").val();
	if ($.trim(user) === '' || $.trim(pass) === '') {
		toggleInputs(false);
		card.text("Please input username and password first!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	}

	const data = {
		username: user,
		password: pass
	};

	await fetch(`/api/${intent}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					card.text(resp.message);
					card.attr("class", "alert alert-success");
					card.show();
					if (intent == 'login'){
						window.location.href = '/feed';
					}
					return;
				}
				card.text(resp.message);
				card.attr("class", "alert alert-danger");
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

	toggleInputs(false); // enable inputs
}