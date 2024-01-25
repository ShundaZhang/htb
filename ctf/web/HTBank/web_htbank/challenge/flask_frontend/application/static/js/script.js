$('#register-link').on('click', () => {
        $('.flip').css('transform', 'rotateY(180deg)');
});

$('#login-link').on('click', () => {
    $('.flip').css('transform', 'rotateY(0deg)');
});

const showMessage = (message) => {
    $('#message').css('display', 'block');
    $('#message').text(message);

    setTimeout(() => {
        $('#message').css('display', 'none');
        $('#message').text('');
    }, 5000)
}

const login = () => {
    const formData = new FormData();

    var username = $('#username_login').val();
    var password = $('#password_login').val();

    if(!$.trim(username).length > 0 || !$.trim(password).length > 0) {
        showMessage('All fields required!');
        return;
    }


    formData.append('username', username);
    formData.append('password', password);

    fetch('/api/login', {
        method: 'POST',
        body: formData
    })
    .then((res) => {
        if(res.status === 200) {
            window.location.replace('/home');
        }
        else {
            showMessage('Invalid credentials');
            return
        }
    })
}

const register = () => {
    const formData = new FormData();

    var username = $('#username_register').val();
    var password = $('#password_register').val();

    if(!$.trim(username).length > 0 || !$.trim(password).length > 0) {
        showMessage('All fields required!');
        return;
    }

    formData.append('username', username);
    formData.append('password', password);



    fetch('/api/register', {
        method: 'POST',
        body: formData
    })
    .then((res) => {
        if(res.status === 200) {
            showMessage('User registered please login!');
        }
        else {
            showMessage('User already exists!');
            return
        }
    })
}