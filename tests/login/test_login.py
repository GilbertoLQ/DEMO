def test_valid_login(login_page, app_config):
    username = app_config.credentials.username
    password = app_config.credentials.password
    login_page.login(username, password)
    assert login_page.is_logged_in()

def test_invalid_login(login_page):
    login_page.login("wronguser", "wrongpass")
    error_msg = login_page.get_error_message()
    assert error_msg is not None
    assert "Your username is invalid!" in error_msg or "Your password is invalid!" in error_msg

def test_empty_credentials(login_page):
    login_page.login("", "")
    flash_text = login_page.get_error_message()
    assert "username" in flash_text.lower() or "password" in flash_text.lower()

def test_password_masking(login_page):
    assert login_page.is_password_masked()

def test_with_screenshot(login_page, request):
    try:
        login_page.login("wrong", "credentials")
        assert False
    except AssertionError:
        screenshot_path = f"screenshots/{request.node.name}.png"
        login_page.driver.save_screenshot(screenshot_path)
        raise
