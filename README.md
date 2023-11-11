# Mobile testing w/ Appium + Python
 
Mobile automation using Appium + Python + Behave 

---
## Setup  

### Sauce Labs setup
1. Free [Sauce account](https://saucelabs.com/sign-up)
2. Make sure you know how to find your Sauce Labs Username and Access Key by going to the [Sauce Labs user settings page](https://app.saucelabs.com/user-settings)

---
### Appium setup
1. We will run our automated tests on Sauce Labs devices; therefore, there is no need to install Appium Server.

---
### Python and Behave setup
1. Install the Python packages: 
2. pip install Appium-Python-Client==3.1.0
3. pip install selenium==4.15.2
4. pip install behave

---
### Demo app(s)   

1. The Android demo apps that has been used for the Android tests can be found [here](https://github.com/saucelabs/my-demo-app-android/releases).

> The advice is to download the files to an `apps` folder in the root of this folder.

Make sure that when you downloaded the files from the releases page, that you rename the apps to the following:

- `mda-{#.#.#-#}.apk` => `my-demo-app-android.apk`

**If you don't do that then the scripts can't find the apps!**

#### Upload apps to Sauce Storage
If you want to use Android emulators, Android real devices, iOS simulators or iOS real devices in the Sauce Labs platform, you need to upload
the apps to the Sauce Storage.

#### Manual upload
Execute the following steps to manually upload the apps:
- Login to the Sauce Labs platform
- Go to **LIVE** > **Mobile App**
- Click on **App Upload** and OR select the folder, OR drag the apps to the screen to upload them


## Run your tests

Run the tests on the Sauce EU DC:

```java
        behave -c

```

## Extra resources

- [Appium options for sauce](https://docs.saucelabs.com/dev/test-configuration-options/#mobile-app-appium-capabilities-required)
- [Appium 2 docs](http://appium.io/docs/en/2.0/)
