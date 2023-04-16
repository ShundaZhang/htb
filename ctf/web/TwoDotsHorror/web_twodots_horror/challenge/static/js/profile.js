$(document).ready(function() {

	// update input label on selection
	$('#avatarFile').change(function() {
		filename = $('input[type=file]')[0].files.length ? $('input[type=file]')[0].files[0].name : "Select profile avatar...";
		$('#file-label').text(filename);
	});

	$("#upload-btn").on('click', upload); // attach event

});



async function upload() {

	$("#upload-btn").prop("disabled", true); // disable multiple submission

	// prepare alert
	let card = $("#resp-msg");
	card.text('Please wait...');

	// validate
	if ($('input[type=file]')[0].files.length == 0) {
		card.text('Please select a file to upload!');
		$("#upload-btn").prop("disabled", false);
		return;
	}

	let avatarFile = $('input[type=file]')[0].files[0];
	let formData = new FormData();
	formData.append('avatarFile', avatarFile);

	await fetch('/api/upload', {
			method: 'POST',
			credentials: 'include',
			body: formData,
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					$(".profile-avatar")[0].src = `/api/avatar/${$('#username').text()}?t=${Math.random()}`; // refresh avatar source 
				}
				avatarFile.value = []; // reset file input
				$('#file-label').text("Select profile avatar..."); // update label
				card.text(resp.message); // set response message
			}))
		.catch((error) => {
			card.text("This file could not be uploaded, please try again!");
		});

	$("#upload-btn").prop("disabled", false);
}