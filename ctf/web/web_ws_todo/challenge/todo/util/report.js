const puppeteer = require('puppeteer')

// please note that 127.0.0.1 and localhost are considered different hosts
// due to ingress networking rules a container can't reach itself through the it's external IP, so you'd have to use the internal ports (80, 8080) and 127.0.0.1

const LOGIN_URL = "http://127.0.0.1/login";

let browser = null

const visit = async (url) => {
    const ctx = await browser.createIncognitoBrowserContext()
    const page = await ctx.newPage()

    await page.goto(LOGIN_URL, { waitUntil: 'networkidle2' })
    await page.waitForSelector('form')
    await page.type('wired-input[name=username]', process.env.USERNAME)
    await page.type('wired-input[name=password]', process.env.PASSWORD)
    await page.click('wired-button')

    try {
        await page.goto(url, { waitUntil: 'networkidle2' })
    } finally {
        await page.close()
        await ctx.close()
    }
}

const doReportHandler = async (req, res) => {

    if (!browser) {
        console.log('[INFO] Starting browser')
        browser = await puppeteer.launch({
            args: [
                "--no-sandbox",
                "--disable-background-networking",
                "--disk-cache-dir=/dev/null",
                "--disable-default-apps",
                "--disable-extensions",
                "--disable-desktop-notifications",
                "--disable-gpu",
                "--disable-sync",
                "--disable-translate",
                "--disable-dev-shm-usage",
                "--hide-scrollbars",
                "--metrics-recording-only",
                "--mute-audio",
                "--no-first-run",
                "--safebrowsing-disable-auto-update",
            ]
        })
    }

    const url = req.body.url
    if (
        url === undefined ||
        (!url.startsWith('http://') && !url.startsWith('https://'))
    ) {
        return res.status(400).send({ error: 'Invalid URL' })
    }

    try {
        console.log(`[*] Visiting ${url}`)
        await visit(url)
        console.log(`[*] Done visiting ${url}`)
        return res.sendStatus(200)
    } catch (e) {
        console.error(`[-] Error visiting ${url}: ${e.message}`)
        return res.status(400).send({ error: e.message })
    }
}

module.exports = { doReportHandler }