from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I have a Behave test')
def step_impl(context):
    print("I am in the given function ")
    products_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.visibility_of_element_located(products_title))

@when('I run the test')
def step_impl(context):
    print("I am in the when function ")
    time.sleep(10)

@then('I see it works')
def step_impl(context):
    print("I am in the then function ")
    # assert False, "Intentionally failing this step"