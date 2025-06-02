from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_fail(appium_driver):
    wait = WebDriverWait(appium_driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-email")))
    username.send_keys("usuario_incorrecto")
    password = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-password")))
    password.send_keys("password_incorrecto")
    login_btn = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-button")))
    login_btn.click()
    assert wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-error")))

def test_login_success(appium_driver):
    wait = WebDriverWait(appium_driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-email")))
    username.send_keys("test@example.com")
    password = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-password")))
    password.send_keys("Test123!")
    login_btn = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "login-button")))
    login_btn.click()
    assert "Login failed" not in appium_driver.page_source