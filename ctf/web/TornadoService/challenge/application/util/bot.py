import time, random, threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def bot_runner(url):
    chrome_options = Options()

    chrome_options.add_argument("headless")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("ignore-certificate-errors")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("disable-background-networking")
    chrome_options.add_argument("disable-default-apps")
    chrome_options.add_argument("disable-extensions")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("disable-sync")
    chrome_options.add_argument("disable-translate")
    chrome_options.add_argument("hide-scrollbars")
    chrome_options.add_argument("metrics-recording-only")
    chrome_options.add_argument("no-first-run")
    chrome_options.add_argument("safebrowsing-disable-auto-update")
    chrome_options.add_argument("media-cache-size=1")
    chrome_options.add_argument("disk-cache-size=1")

    client = webdriver.Chrome(options=chrome_options)

    client.get(url)
    time.sleep(10)

    client.quit()

def bot_thread(url):
    thread = threading.Thread(target=bot_runner, args=(url,))
    thread.start()
    return thread