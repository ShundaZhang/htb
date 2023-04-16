const puppeteer = require('puppeteer');

const browser_options = {
	headless: true,
	args: [
		'--no-sandbox',
		'--disable-background-networking',
		'--disable-default-apps',
		'--disable-extensions',
		'--disable-gpu',
		'--disable-sync',
		'--disable-translate',
		'--hide-scrollbars',
		'--metrics-recording-only',
		'--mute-audio',
		'--no-first-run',
		'--safebrowsing-disable-auto-update'
	]
};

const cookies = [{
    'name': 'flag',
    'value': 'HTB{f4k3_fl4g_f0r_t3st1ng}'
}];

async function purgeData(db){
	const browser = await puppeteer.launch(browser_options);
	const page = await browser.newPage();

	await page.goto('http://127.0.0.1:1337/');
	await page.setCookie(...cookies);

	await page.goto('http://127.0.0.1:1337/review', {
		waitUntil: 'networkidle2'
	});

	await browser.close();
	await db.migrate();
};

module.exports = { purgeData };