$(document).ready(() => {
	loadEntries();
	$('#searchBtn').on('click', searchEntry);
	$('#searchQuery').keypress(() => $('#resp-msg').hide());
});

const loadEntries = async () => {
	await fetch(`/api/entries`, {
			method: 'GET',
			credentials: 'include'
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					$(resp).each((k, entry) => {
						entryHTML = `<div class="card text-white bg-secondary mb-3 card-ovrwr">
								  <div class="card-header">Title: ${entry.title}</div>
								  <div class="card-body">
								    <p class="card-text">${entry.url}</p>
								  	<span class="badge bg-danger">${(entry.approved == 1) ? 'approved' : 'unapproved'}</span>
								  </div>
								</div>`;
						$('#entries-container').append(entryHTML);
					})
				}

			}))
		.catch((error) => {

		});
}


const searchEntry = async () => {
	$("#searchBtn").prop('disabled', true);
	const card = $('#resp-msg');
	const query = encodeURIComponent($('#searchQuery').val());

	if ($.trim(query) === '') {
		card.text('Please input search query first!');
		card.show();
		$("#searchBtn").prop('disabled', false);
		return;
	}

	await fetch(`/api/entries/search?q=${query}`, {
			method: 'GET',
			credentials: 'include'
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					$('#entries-container').html('');
					$(resp).each((k, entry) => {
						entryHTML = `<div class="card text-white bg-secondary mb-3 card-ovrwr">
								  <div class="card-header">Title: ${entry.title}</div>
								  <div class="card-body">
								    <p class="card-text">${entry.url}</p>
								  	<span class="badge bg-danger">${(entry.approved == 1) ? 'approved' : 'unapproved'}</span>
								  </div>
								</div>`;
						$('#entries-container').append(entryHTML);
					});
				} else {
					$('#entries-container').html('');
					card.text(resp.message);
					card.show();
				}
			}))
		.catch((error) => {
			card.text(error);
			card.show();
		});
	$("#searchBtn").prop('disabled', false);
}

