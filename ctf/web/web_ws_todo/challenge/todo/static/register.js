const form = document.getElementById('register-form');

const formHandler = async () => {
    const username = form.querySelector('#username').value;
    const password = form.querySelector('#password').value;
    const password2 = form.querySelector('#confirm').value;

    if (password !== password2) {
        Swal.fire({
            title: 'Oops...',
            text: 'Passwords do not match!',
            icon: 'error'
        });
        return;
    }

    const res = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    if (res.status === 200) {
        Swal.fire({
            title: 'Success!',
            text: 'You have successfully registered!',
            icon: 'success'
        });
        setTimeout(() => {
            window.location.href = '/login';
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