const createNode = elem => {
  return document.createElement(elem)
}

const appendNode = (parent, elem) => {
  parent.appendChild(elem)
}

let alert = document.getElementById('alerts')
let secret = document.getElementById('data-secret').value

const flash = (category, message) => {
  let div = createNode('div'),
  strong = createNode('strong'),
  button = createNode('button'),
  span = createNode('span')

  div.className = `alert alert-${category} alert-dismissible fade show`
  div.setAttribute('role', 'alert')

  strong.innerHTML = message

  button.className = 'close'
  button.setAttribute('type', 'button')
  button.setAttribute('data-dismiss', 'alert')
  button.setAttribute('aria-label', 'Close')

  button.onclick = () => {
    div.style.opacity = 0
    setTimeout(() => {
      div.remove()
    }, 300)
  }

  span.setAttribute('aria-hidden', 'true')
  span.innerHTML = '&times;'

  appendNode(div, strong)
  appendNode(button, span)
  appendNode(div, button)
  appendNode(alert, div)

  setTimeout(() => {
    button.click()
  }, 2800)
}

const ul = document.querySelector('#tasks')
const form = document.getElementById('add')

const toJSONString = elem => {
  return JSON.stringify({
    name: elem.value,
    secret: secret
  })
}

const add = task => {
  return fetch('/api/add/', {
    method: 'POST',
    body: task,
    headers: {
      'Content-Type': 'application/json',
    }
  })
}

const complete = task => fetch(`/api/complete/${task.id}/?secret=${secret}`, {method: 'GET'})

const delet = task => fetch(`/api/delete/${task.id}/?secret=${secret}`, {method: 'DELETE'})

const create_list = task => {
  let li = createNode('li'),
  span = createNode('span'),
  div = createNode('div'),
  com = createNode('button'),
  del = createNode('button'),
  error = '[+] Oops, something went wrong!'
  
  li.className = 'flex'
  span.innerHTML = task.name
  div.className = 'space'

  if (task.done) {
    com.className = 'nes-btn is-disabled'
    com.innerHTML = 'Completed'
  } else {
    com.className = 'nes-btn is-success'
    com.innerHTML = 'Complete'
  }

  com.onclick = () => {
    if (task.done) return
    complete(task).then(res => {
      update()
      if (res.ok) {
        flash('success', `[*] Successfuly completed ${task.id}`)
        com.className = 'nes-btn is-disabled'
        com.innerHTML = 'Completed'
        update()
      } else {
        flash('danger', error)
      }
    })
  }

  del.className = 'nes-btn is-error'
  del.innerHTML = 'Delete'

  del.onclick = () => {
    delet(task).then(res => {
      update()
      if (res.ok) {
        flash('success', `[*] Successfuly deleted ${task.id}`)
      } else {
        flash('danger', error)
      }
    })
  }
  appendNode(li, span)
  appendNode(li, div)
  appendNode(li, com)
  appendNode(li, del)
  appendNode(ul, li)
}

const getTasks = endpoint => {
  fetch(`/api/list/${endpoint}/?secret=${secret}`).then(res => {
    if (res.ok) {
      res.json().then(data => {
        ul.innerHTML = ''
        data.map(task => {
          create_list(task)
        })
      })
    } else {
      window.location.reload(true)
    }
  })
}

form.addEventListener('submit', e => {
  e.preventDefault()
  let task = document.querySelector('input[type=text]')
  add(toJSONString(task)).then(res => {
    document.getElementById('add-task').value = ''
    update()
    if (res.ok) {
      flash('success', `[*] Successfuly added ${task.value}`)
    } else {
      flash('danger', '[+] Server refused to process your todo task')
    }
  })
})