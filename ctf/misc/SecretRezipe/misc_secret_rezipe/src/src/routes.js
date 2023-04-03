const { Router } = require('express')
const child_process = require('child_process')
const fs = require('fs')
const crypto = require('crypto');
const path = require('path');
const os = require('os');

const { FLAG, PASSWORD } = require('./config/config')

const router = Router()

router.post('/ingredients', (req, res) => {
  let data = `Secret: ${FLAG}`

  if (req.body.ingredients) {
    data += `\n${req.body.ingredients}`
  }

  const tempPath = os.tmpdir() + '/' + crypto.randomBytes(16).toString('hex')
  fs.mkdirSync(tempPath);
  fs.writeFileSync(tempPath + '/ingredients.txt', data)
  child_process.execSync(`zip -P ${PASSWORD} ${tempPath}/ingredients.zip ${tempPath}/ingredients.txt`)
  return res.sendFile(tempPath + '/ingredients.zip')
})

router.get('/*', (_, res) => res.sendFile(__dirname + '/static/index.html'))

module.exports = router
