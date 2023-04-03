const express = require('express')

const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(express.static(__dirname + '/static'))
app.use(require('./routes'))

app.listen(1337, () => console.log('Listening on port 1337'))
