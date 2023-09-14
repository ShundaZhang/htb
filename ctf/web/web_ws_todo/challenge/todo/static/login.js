const form = document.getElementById('login-form');

const formHandler = async () => {
    const username = form.querySelector('#username').value;
    const password = form.querySelector('#password').value;

    const res = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    if (res.status === 200) {
        Swal.fire({
            title: 'Success!',
            text: 'You have been logged in!',
            icon: 'success'
        });
        setTimeout(() => {
            window.location.href = '/';
        }, 2000);
        return;
    }

    const data = await res.json();
    Swal.fire({
        title: 'Oops...',
        text: data.error,
        icon: 'error'
    });

}

form.querySelector('wired-button').addEventListener('click', (e) => {
    try { formHandler() } catch {}
});