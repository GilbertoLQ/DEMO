import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")  # Desactiva TODAS las extensiones
    options.add_argument("--incognito")  # Modo incógnito también evita autofills
    #options.add_argument("--headless")  # Puedes quitar esto si quieres ver el navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver)