from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser="chrome", headless=False):
    browser = browser.lower()
    options = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
