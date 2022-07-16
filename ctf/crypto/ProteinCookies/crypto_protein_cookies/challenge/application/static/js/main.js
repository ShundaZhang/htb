let alerts  = document.getElementById('alerts');
let form    = document.getElementById('form');

const flash = (message, level) => {
    alerts.innerHTML += `
        <div class="alert alert-${level}" role="alert" style="padding-top: 5px;">
            <button type="button" id="closeAlert" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <strong>${message}</strong>
        </div>
    `;

    setTimeout(() => {
        document.getElementById('closeAlert').click();
    }, 3000);
};

let urlParams = new URLSearchParams(window.location.search)

if (urlParams.has('error')) {
    flash(urlParams.get('error'), 'danger')
};

form.addEventListener('submit', e => {
    e.preventDefault();

    alerts.innerHTML = '';

    fetch(`/api${window.location.pathname}`, {
        method: 'POST',
    })
        .then(resp => {
            return resp.json();
        })
        .then(data => {
            if (data.error) {
                flash(data.message, 'danger')

                return 0;
            }
    });
});