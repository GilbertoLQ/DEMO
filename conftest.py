import pytest
from utils.driver_manager import get_driver
from utils.appium_manager import get_appium_driver
from pages.login_page import LoginPage
from config import load_app_config

@pytest.fixture(scope="session")
def appium_driver():
    driver = get_appium_driver(
        platform_name="iOS",
        device_name="iPhone 15 Pro Max",
        app_path="/Users/Gil/Downloads/PaypalClone.app",  # Cambia esta ruta a tu .app real
        platform_version="17.2",
    )
    yield driver
    driver.quit()

@pytest.fixture(scope="session") # Carga la configuración de la app según el entorno (dev/prod).
def app_config():
    return load_app_config("dev")

@pytest.fixture(scope="session")
def driver(app_config):
    driver = get_driver(
        headless=app_config.headless,
        browser=app_config.browser
    )
    yield driver
    driver.quit()

@pytest.fixture
def setup(driver, app_config): # Prepara el entorno: navega a la URL base antes de cada test.
    driver.get(app_config.base_url)
    yield driver

@pytest.fixture
def login_page(setup): # Devuelve una instancia de LoginPage ya inicializada en la URL base.
    return LoginPage(setup)
