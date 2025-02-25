from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
#PLATFORM = "Android"
PLATFORM = "iOS"  # Change to "Android" for Android testing
APP_PATHS = {
    "Android": "/Users/aungwaiwaithin/Documents/dfi-latest-staging-release.apk",
    "iOS": "/Users/aungwaiwaithin/Documents/Payload/DFIPreferred.app",
}
PACKAGE_NAMES = {
    "Android": "com.coldstorage.staging",
    "iOS": "enterprise.codigo.dfipreferred",
}
UDID_IOS = "00008030-001924CC1488802E"  # iOS real device UDID
DEVICE_NAME_IOS = "iPhone 11"  # iOS real device name

# Locators
NEXT_BUTTON = {
    "Android": 'btnArrow',
    "iOS": '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton[1]',
}
EMPLOYEE_ID = "textFieldEmployeeId"
EMPLOYEE_FULL_NAME = "textFieldFullName"
ERROR_EMPLOYEE_ID = "errorEmployeeId"
ERROR_FULL_NAME = "errorFullName"
SELECT_SPOUSE_ID = "btnSpouse"
MOBILE_NUMBER_DROPDOWN_ID = "dropDownMobileCode"
MOBILE_NUMBER_SG_ID = "itemSingapore"
MOBILE_NUMBER_MY_ID = "itemMalaysia"
MOBILE_NUMBER_TEXTBOX_ID = "textFieldMobileNumber"
ERROR_MSG_MOBILE = "errorMobileNumber"
AGREE_CHECKBOX_ID = "checkBoxAgree"
CONTINUE_BUTTON = "Continue"
OTP_FIELD = "textFieldOTP"
ERROR_OTP = "lblOTPError"


class DFI:
    def __init__(self):
        if PLATFORM == "Android":
            self.options = UiAutomator2Options()
            self.options.set_capability("appium:ignoreHiddenApiPolicyError", True)
            self.options.set_capability("platformName", "Android")
            self.options.set_capability("app", APP_PATHS["Android"])
        elif PLATFORM == "iOS":
            self.options = XCUITestOptions()
            self.options.set_capability("platformName", "iOS")
            self.options.set_capability("app", APP_PATHS["iOS"])
            self.options.set_capability("udid", UDID_IOS)
            self.options.set_capability("deviceName", DEVICE_NAME_IOS)

        self.URL = "http://127.0.0.1:4723"
        self.driver = webdriver.Remote(self.URL, options=self.options)

    def test_uninstall_app(self):
        print("---------------------uninstall-----------------------")
        package_name = PACKAGE_NAMES[PLATFORM]
        if self.driver.is_app_installed(package_name):
            self.driver.remove_app(package_name)
            print("Old app Uninstall Successfully!!!")
        else:
            print("-------------There is no app installed-------------")

    def test_install_app(self):
        print("---------------------install-----------------------")
        self.driver.install_app(APP_PATHS[PLATFORM])
        time.sleep(5)
        print("New app is installed: ", self.driver.is_app_installed(PACKAGE_NAMES[PLATFORM]))

    def test_launch_app(self):
        print("---------------------launch-----------------------")
        time.sleep(5)
        self.driver.activate_app(PACKAGE_NAMES[PLATFORM])
        print("🚀 App launched successfully!")

    def test_validation_message(self):
        print("---------------------Validation Check-----------------------")
        time.sleep(5)
        if PLATFORM == "Android":
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, NEXT_BUTTON[PLATFORM]).click()
        else:
            self.driver.find_element(AppiumBy.XPATH, NEXT_BUTTON[PLATFORM]).click()
        time.sleep(5)

        # Invalid Employee ID
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_ID).send_keys("11000136")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_FULL_NAME).send_keys("Das Daisy")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECT_SPOUSE_ID).click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_DROPDOWN_ID).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_MY_ID).click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).send_keys("99999996")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, AGREE_CHECKBOX_ID).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON).click()
        time.sleep(5)

        acc_not_exist = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ERROR_EMPLOYEE_ID).text
        print("Incorrect Employee ID: " + acc_not_exist)

        # Invalid Full Name
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_ID).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_ID).send_keys("11000135")
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_FULL_NAME).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_FULL_NAME).send_keys("Das Daisy Incorrect")
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON).click()
        time.sleep(5)
        full_name_incorrect = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ERROR_FULL_NAME).text
        print("Incorrect Full Name: " + full_name_incorrect)

        # Invalid Malaysia Mobile Number
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_FULL_NAME).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, EMPLOYEE_FULL_NAME).send_keys("Das Daisy")
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).send_keys("1234")
        time.sleep(5)
        mobile_invalid = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ERROR_MSG_MOBILE).text
        print("Incorrect Malaysia Mobile Number: " + mobile_invalid)

        # Invalid Singapore Mobile Number
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_DROPDOWN_ID).click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_SG_ID).click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).send_keys("123")
        time.sleep(5)
        mobile_invalid = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ERROR_MSG_MOBILE).text
        print("Incorrect Singapore Mobile Number: " + mobile_invalid)

    def test_login(self):
        print("---------------------Login-----------------------")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).clear()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, MOBILE_NUMBER_TEXTBOX_ID).send_keys("99999996")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON).click()
        print("Navigated to OTP screen")

    def test_invalid_otp(self):
        print("---------------------Invalid OTP--------------------------")
        time.sleep(5)  # Wait for the OTP screen to load

        # Enter invalid OTP
        otp_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, OTP_FIELD)
        otp_field.send_keys("1111")

        # Wait for the OTP error message to appear
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        otp_error_element = wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, ERROR_OTP)))
        otp_error_msg = otp_error_element.text
        print("OTP Error: " + otp_error_msg)

        # if PLATFORM == "Android":
        #     otp_error_element = wait.until(
        #         EC.presence_of_element_located((AppiumBy.XPATH, ERROR_OTP["Android"])))
        # else:
        #     otp_error_element = wait.until(
        #         EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, ERROR_OTP["iOS"])))
        # otp_error_msg = otp_error_element.text
        # print("OTP Error: " + otp_error_msg)

    def test_valid_otp(self):
        print("---------------------Valid OTP--------------------------")
        time.sleep(5)  # Wait for the OTP screen to load

        otp_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, OTP_FIELD)
        otp_field.clear()
        otp_field.send_keys("1234")
        if PLATFORM == "iOS":
            for i in range(1, 5):
                otp_field_xpath = f'//XCUIElementTypeOther[@name="textFieldOTP"]/XCUIElementTypeTextField[{i}]'
                self.driver.find_element(AppiumBy.XPATH, otp_field_xpath).clear()
            time.sleep(2)
            otp = "1234"
            for i, digit in enumerate(otp, start=1):
                otp_field_xpath = f'//XCUIElementTypeOther[@name="textFieldOTP"]/XCUIElementTypeTextField[{i}]'
                self.driver.find_element(AppiumBy.XPATH, otp_field_xpath).send_keys(digit)
                time.sleep(1)
        print("OTP Valid Successfully!")

    def main(self):
        self.test_uninstall_app()
        self.test_install_app()
        self.test_launch_app()
        self.test_validation_message()
        self.test_login()
        self.test_invalid_otp()
        self.test_valid_otp()


if __name__ == "__main__":
    DFI().main()