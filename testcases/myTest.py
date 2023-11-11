# pip install Appium-Python-Client==3.1.0
# pip install selenium==4.15.2
# pip install behave
import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


app = "my-demo-app-android.apk"
dc = {'platformName': 'Android'}
dc['appium:automationName'] = 'UiAutomator2'
dc['appium:app'] = "storage:filename=" + app
dc['appium:autoGrantPermissions'] = True
dc['appium:deviceName'] = "Samsung.*"
dc['appium:platformVersion'] = "1[3-4]"
# Set Sauce Credentials in Path
dc['sauce:options'] = {"name": "My test"}
dc['sauce:options']["username"] = os.environ["SAUCE_USERNAME"]
dc['sauce:options']["accessKey"] = os.environ["SAUCE_ACCESS_KEY"]

url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
print("Desired Capabilities (dc): ", dc)
options = UiAutomator2Options().load_capabilities(dc)
driver = webdriver.Remote(url, options=options)
driver.implicitly_wait(60)

time.sleep(10)

driver.quit()