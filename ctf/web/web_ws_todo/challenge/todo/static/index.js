const tasks = document.getElementById('tasks');
const taskForm = document.getElementById('task-form');

const ws = new WebSocket(`ws://${window.location.host}/ws`);

const showTask = (task) => {
    const taskElement = document.createElement('div');
    taskElement.classList.add('task');
    taskElement.appendChild(document.createElement('h3')).appendChild(document.createElement('wired-checkbox')).innerText = task.title.content;
    taskElement.appendChild(document.createElement('p')).innerText = task.description.content;
    taskElement.appendChild(document.createElement('p')).appendChild(document.createElement('i')).innerText = task.quote.content;
    tasks.appendChild(taskElement);
};

const decrypt = async (cipher, secret) => {
    const res = await fetch('/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cipher, secret })
    });

    const json = await res.json();
    return json.decrypted;
}

ws.onopen = () => {
    ws.send(JSON.stringify({ action: 'get' }));
}

ws.onmessage = async (msg) => {
    const data = JSON.parse(msg.data);
    if (data.success) {
        if (data.action === 'get') {
            const secret = await fetch('/secret').then(res => res.json()).then(data => data.secret);
            for (const task of data.tasks) {
                showTask({
                    title: {
                        iv: task.title.iv,
                        content: await decrypt(task.title, secret)
                    },
                    description: {
                        iv: task.description.iv,
                        content: await decrypt(task.description, secret)
                    },
                    quote: {
                        iv: task.quote.iv,
                        content: await decrypt(task.quote, secret)
                    }
                });
            }
        }
        else if (data.action === 'add') {
            taskForm.reset();
        }
    }
    else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: data.error
        });
    }
}

const formHandler = async () => {
    const title = taskForm.querySelector('#title').value;
    const description = taskForm.querySelector('#description').value;

    ws.send(JSON.stringify({ action: 'add', title, description }));
    
    tasks.innerHTML = '';
    ws.send(JSON.stringify({ action: 'get' }));

    Swal.fire({
        icon: 'success',
        title: 'Success!',
        text: 'Task added!'
    });
}

taskForm.querySelector('wired-button').addEventListener('click', (e) => {
    try { formHandler() } catch { }
});