let canvas = document.getElementById('galaxy');
let ctx = canvas.getContext('2d');
canvas.width = innerWidth;
canvas.height = innerHeight;

let deathstar = {
	image: new Image(),
	laser: 0,
	x: innerWidth + 100,
	y: innerHeight / 2 - 150,
	update: function () {
		this.x = this.x - 1;
		this.laser--;
	},
	draw: function () {
		if (this.laser > 0) {
			ctx.save();
			ctx.beginPath();
			ctx.lineWidth = 5;
			ctx.strokeStyle = '#FFF';
			ctx.shadowColor = '#00960a';
			ctx.shadowOffsetX = 0;
			ctx.shadowOffsetY = 0;
			ctx.shadowBlur = 20;
			ctx.moveTo(deathstar.x + 85, deathstar.y + 75);
			ctx.lineTo(0, deathstar.y + 75);
			ctx.stroke();
			ctx.restore();
		}
	} };

deathstar.image.src = '//cdn.rawgit.com/ManzDev/codevember2017/master/assets/death-star-256x256.png';

window.onresize = function () {
	canvas.width = innerWidth;
	canvas.height = innerHeight;
};

function clearScreen() {
	ctx.fillStyle = '#000';
	ctx.fillRect(0, 0, canvas.width, canvas.height);
}

let stars = [];
for (let i = 0; i < 500; i++) {
	stars.push({
		x: ~~(Math.random() * canvas.width),
		y: ~~(Math.random() * canvas.height),
		speed: ~~(1 + Math.random() * 5),
		color: ~~(Math.random() * 3) });

}

function loop() {
	requestAnimationFrame(loop, canvas);
	update();
	render();
}

function update() {

	for (let i = 0; i < 500; i++) {
		stars[i].x -= stars[i].speed;
		if (stars[i].x < 0)
		stars[i].x = canvas.width;
	}

	deathstar.update();

}

function render() {

	clearScreen();
	for (let i = 0; i < 500; i++) {
		var s = stars[i];
		ctx.lineWidth = 1;
		ctx.strokeStyle = ['#444', '#888', '#FFF'][stars[i].color];
		ctx.strokeRect(s.x, s.y, 1, 1);
	}

	if (~~(Math.random() * 250) == 1)
	deathstar.laser = 15 + ~~(Math.random() * 25);

	ctx.drawImage(deathstar.image, deathstar.x, deathstar.y);
	deathstar.draw();
}

loop();
let music = new Audio('//cdn.rawgit.com/ManzDev/codevember2017/master/assets/imperial-8bit-by-crig.mp3');

document.addEventListener('click', () => {
	music.volume = 0.03
    music.play();

});

document.getElementById('form').addEventListener('submit', e => {
	e.preventDefault();

	fetch('/api/calculate', {
		method: 'POST',
		body: JSON.stringify({
			name: document.querySelector('input[type=radio]:checked').value
		}),
		headers: {'Content-Type': 'application/json'}
	}).then(resp => {
		return resp.json();
	}).then(data => {
		document.getElementById('output').innerHTML = data.pass;
	});

});