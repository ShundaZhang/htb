from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os


def bot(url):

    options = Options()
    os.environ["MOZ_DISABLE_CONTENT_SANDBOX"] = "1"
    os.environ["MOZ_CRASHREPORTER_DISABLE"] = "1"
    options.headless = True
    options.set_preference("general.useragent.override", "TorBrowser/1.0")
    binary = FirefoxBinary("/firefox/firefox")
    browser = webdriver.Firefox(firefox_binary=binary, options=options)

    try:
        browser.get(url)
        WebDriverWait(browser, 5).until(
            lambda r: r.execute_script("return document.readyState") == "complete"
        )
    except:
        pass
    finally:
        browser.quit()

if __name__ == '__main__':
    url = input("Enter URL for bot: ")
    bot(url)

