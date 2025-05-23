import pytest
from utils.driver_manager import get_driver
from pages.login_page import LoginPage
from config import load_app_config  # Usamos el loader de configuraciones

@pytest.fixture(scope="session") #Carga la configuración según el entorno (dev/prod).
def app_config():
    return load_app_config("dev") #se puede cambiar dependiendo del env

@pytest.fixture
def driver(app_config): # WebDriver configurado según el YAML
    driver = get_driver(
        headless=app_config.headless,  # Usa el valor del YAML
        browser=app_config.browser    # Ejemplo: "chrome" o "firefox"
    )
    yield driver
    driver.quit()

@pytest.fixture
def setup(driver, app_config): #Prepara el entorno: navega a la URL base
    driver.get(app_config.base_url)  # URL desde YAML
    yield driver

@pytest.fixture
def login_page(setup):
    return LoginPage(setup)
