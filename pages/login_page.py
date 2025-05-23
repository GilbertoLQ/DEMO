from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username: str, password: str):
        self.load()
        # Esperar que el campo username esté visible y luego enviar texto
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username_field.clear()
        username_field.send_keys(username)

        # Esperar que el campo password esté visible y luego enviar texto
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)

        # Esperar que el botón esté clickable y hacer click
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius")))
        login_button.click()

    def is_login(self):
        # Espera hasta que la url contenga "secure" o timeout
        try:
            self.wait.until(EC.url_contains("secure"))
            return True
        except:
            return False
    
    def is_password_masked(self,masked_check=False):
        self.load()
        element_type = self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).get_attribute("type")
        return element_type == "password" if masked_check else element_type

    def get_error_message(self):
        # Método para obtener mensaje de error si hay
        try:
            error_div = self.wait.until(EC.visibility_of_element_located((By.ID, "flash")))
            return error_div.text
        except:
            return None
        
    def get_flash_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text.strip()
