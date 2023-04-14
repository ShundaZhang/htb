const stampContainer = document.getElementById('stamp-container');
const sendMessage = document.getElementById('send-message');
const input = document.getElementById('letter-content');

const typeMessage = (message) => {
    sendMessage.innerText = '';
    sendMessage.style.display = '';

    message.split('').forEach((char, index) => {
        setTimeout(() => {
            sendMessage.innerHTML += char;
        }, index * 100);
    });
};

stampContainer.addEventListener('click', (event) => {
    if (stampContainer.classList.contains('stamped')) return;

    typeMessage('Sending your letter...');
    stampContainer.classList.add('stamped');

    fetch('/submit', {
            method: 'POST',
            body: JSON.stringify({
                message: input.value,
            }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .catch(error => {
            typeMessage(error);
        })
        .then(response => response.json()
            .then(data => {
                if (response.status !== 201) {
                    typeMessage(data.message);
                } else {
                    setTimeout(() => {
                        window.location = '/letters?id=' + data.message;
                    }, 2500);
                }
            }));
});