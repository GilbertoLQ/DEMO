def test_ios_app_launch(appium_driver):
    # Ejemplo: verifica que la app se inicia correctamente en iOS
    assert appium_driver.capabilities["platformName"] == "iOS"