$(document).ready(() => {
    $('#approveBtn').on('click', approve);
    $('#rejectBtn').on('click', reject);
});

const approve = async (e) => {
    var btn = $(e.target);
    btn.prop('disabled', true);

	let responseBox = $('#responseMsg');
	responseBox.attr('class', 'alert alert-info mt-3');
	responseBox.hide();

	await fetch('/approve/' + btn.data("id") + "/" + $('#approvalToken').text())
		.then((response) => response.json()
			.then((resp) => {
				responseBox.attr('class', 'alert alert-danger mt-3');
				if (response.status == 200) {
					responseBox.attr('class', 'alert alert-success mt-3');
				}
				responseBox.text(resp.message);
				responseBox.show();
			}))
		.catch((error) => {
			responseBox.text(error);
			responseBox.attr('class', 'alert alert-danger mt-3');
			responseBox.show();
		});

        btn.prop('disabled', false);
}

const reject = async (e) => {
    var btn = $(e.target);
    btn.prop('disabled', true);

	let responseBox = $('#responseMsg');
	responseBox.attr('class', 'alert alert-info mt-3');
	responseBox.hide();

	await fetch('/reject/' + btn.data("id") + "/" + $('#rejectToken').text())
		.then((response) => response.json()
			.then((resp) => {
				responseBox.attr('class', 'alert alert-danger mt-3');
				if (response.status == 200) {
					responseBox.attr('class', 'alert alert-success mt-3');
				}
				responseBox.text(resp.message);
				responseBox.show();
			}))
		.catch((error) => {
			responseBox.text(error);
			responseBox.attr('class', 'alert alert-danger mt-3');
			responseBox.show();
		});

        btn.prop('disabled', false);
}