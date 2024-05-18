
module.exports = {
	generateToken() {
		const dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		const shuffle = v=>[...v].sort(_=>Math.random()-.5).join('');

		// Shuffle characters and sort them in ASCII order
		return shuffle(dict).substring(0, 32).split('').sort().join('');
	}
}