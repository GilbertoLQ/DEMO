from appium import webdriver
from appium.options.common import AppiumOptions

def get_appium_driver(
    platform_name="iOS",
    device_name="iPhone Simulator",
    platform_version="17.2",
    app_path=None,
    udid=None,
):
    if not app_path:
        raise ValueError("app_path must be provided for Appium driver initialization")
    
    options = AppiumOptions()
    options.set_capability("platformName", platform_name)
    options.set_capability("deviceName", device_name)
    options.set_capability("automationName", "XCUITest")
    options.set_capability("platformVersion", platform_version)
    options.set_capability("app", app_path)
    options.set_capability("wdaLaunchTimeout", 120000)
    options.set_capability("noReset", True)
    options.set_capability("fullReset", False)
    
    if udid:
        options.set_capability("udid", udid)

    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )
    return driver