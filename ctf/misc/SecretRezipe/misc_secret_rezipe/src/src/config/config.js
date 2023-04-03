const crypto = require('crypto')
const fs = require('fs')

try {
     var FLAG = fs.readFileSync("/flag.txt")
} catch (e) {
    var FLAG = "HTB{fake_flag_for_testing}"
}
module.exports = {
  FLAG: FLAG,
  PASSWORD: crypto.randomUUID()
}
