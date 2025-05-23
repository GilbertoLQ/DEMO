from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def login(self, username: str, password: str):
        username_input = self.wait_for_element_visible(By.ID, "username")
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.wait_for_element_visible(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

        login_btn = self.wait_for_element_clickable(By.CSS_SELECTOR, "button.radius")
        login_btn.click()

    def is_logged_in(self) -> bool:
        try:
            self.wait.until(EC.url_contains("secure"))
            return True
        except TimeoutException:
            return False

    def is_password_masked(self) -> bool:
        try:
            password_input = self.wait_for_element_visible(By.ID, "password")
            return password_input.get_attribute("type") == "password"
        except TimeoutException:
            return False

    def get_error_message(self) -> str | None:
        try:
            error_div = self.wait_for_element_visible(By.ID, "flash")
            return error_div.text.strip()
        except TimeoutException:
            return None
        
    def wait_for_element_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_element_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))


