# pip install Appium-Python-Client==3.1.0
# pip install selenium==4.15.2
# pip install behave
# pip install requests
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
import requests
import json


def before_scenario(context, scenario):
    # Code to run before each scenario
    print("I am in the before function ")
    app = "my-demo-app-android.apk"
    dc = {'platformName': 'Android'}
    dc['appium:automationName'] = 'UiAutomator2'
    dc['appium:app'] = "storage:filename=" + app
    dc['appium:autoGrantPermissions'] = True
    dc['appium:deviceName'] = "Samsung.*"
    dc['appium:platformVersion'] = "1[3-4]"
    # Set Sauce Credentials in Path
    dc['sauce:options'] = {"name": scenario.name}
    dc['sauce:options']["username"] = os.environ["SAUCE_USERNAME"]
    dc['sauce:options']["accessKey"] = os.environ["SAUCE_ACCESS_KEY"]

    url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
    # print("Desired Capabilities (dc): ", dc)
    options = UiAutomator2Options().load_capabilities(dc)
    context.driver = webdriver.Remote(url, options=options)
    context.driver.implicitly_wait(60)

def after_scenario(context, scenario):
    # Code to run after each scenario
    job_id = ""
    try:
        # Execute the script to set the job result in Sauce Labs
        status = 'passed' if scenario.status == 'passed' else 'failed'
        context.driver.execute_script(f"sauce:job-result={status}")

        # Get the session ID
        capabilities = context.driver.capabilities
        print("Sauce - capabilities id is: ", capabilities)
        job_id = str(capabilities['jobUuid'])
        print("Sauce - job id is: ", job_id )

    finally:
        print("Sauce - release driver")
        context.driver.quit()

        # To get the Job info
        api_url = f"https://api.eu-central-1.saucelabs.com/v1/rdc/jobs/{job_id}"
        session = requests.Session()
        session.auth = (os.environ["SAUCE_USERNAME"], os.environ["SAUCE_ACCESS_KEY"])
        try:
            # Send a GET request to the API
            response = session.get(api_url)

            # Check if the request was successful (HTTP status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                api_data = response.json()

                # Print the JSON data or perform further processing
                print(json.dumps(api_data, indent=4))
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        # Close the session
        session.close()