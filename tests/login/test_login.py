from pages.login_page import LoginPage

def test_valid_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.is_login()

def test_invalid_login(login_page):
    login_page.login("wronguser", "wrongpass")
    assert not login_page.is_login()
    error_msg = login_page.get_error_message()
    assert error_msg is not None
    assert "Your username is invalid!" in error_msg or "Your password is invalid!" in error_msg

def test_empty_credentials(login_page):
    login_page.login("", "")
    assert not login_page.is_login()
    # Verifica el mensaje flash en lugar de validación de campos
    flash_text = login_page.get_flash_message()
    assert "username" in flash_text.lower() or "password" in flash_text.lower()

def test_password_masking(login_page):
    assert login_page.is_password_masked(masked_check=True)

# def test_login_form_styling(login_page):
#     assert login_page.is_login_button_visible()
#     assert login_page.is_login_button_enabled()
#     assert login_page.get_login_button_text() == "Login"


def test_with_screenshot(login_page, request):
    try:
        login_page.login("wrong", "credentials")
        assert False
    except AssertionError:
        screenshot_path = f"screenshots/{request.node.name}.png"
        login_page.driver.save_screenshot(screenshot_path)
        raise
