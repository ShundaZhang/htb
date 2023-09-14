const crypto = require('crypto');

const algorithm = 'aes-256-ctr';

const encrypt = (text, key) => {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(algorithm, key, iv);
    const encrypted = Buffer.concat([cipher.update(text), cipher.final()]);
    return {
        iv: iv.toString('hex'),
        content: encrypted.toString('hex')
    };
};

const decrypt = (cipher, key) => {
    const decipher = crypto.createDecipheriv(algorithm, key, Buffer.from(cipher.iv, 'hex'));
    const decrpyted = Buffer.concat([decipher.update(Buffer.from(cipher.content, 'hex')), decipher.final()]);
    return decrpyted.toString();
};

module.exports = {
    encrypt,
    decrypt
};