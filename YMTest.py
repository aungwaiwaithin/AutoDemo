from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select
from pyotp import random

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestYoGa:

    driver = webdriver.Chrome()

    def test_open_browser(self):
        self.driver.get("https://webfront-uat.yogamovement.com/")
        time.sleep(10)
        #self.driver.get("https://www.yogamovement.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"/html/body/div/div/aside/div/div[2]/button").click()
        print("Test 1 : Open browser success!")
        time.sleep(3)

    def test_register_test(self):
        print ("success 01")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()
        time.sleep(2)
        print ("success 02")
        #user_email = "waiwai47@yopmail.com"

        user_pwd="awwt47"

        #Random number for email postfix
        r_n_f_email=[random.randint(0,9) for i in range(2)]
        pffm="".join(str(x) for x in r_n_f_email)
        rue="WaiWai"+pffm+"@yopmail.com"
        self.driver.find_element(By.NAME, "email").send_keys(rue)
        print ("success 03")

        #Enter pwd
        self.driver.find_element(By.NAME, "password").send_keys(user_pwd, Keys.RETURN)
        print ("Entering username and pwd scuccess")
        time.sleep(5)

        #Enter first name and Last name
        self.driver.find_element(By.NAME, "firstname").send_keys("Aung")
        print ("success 05")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("WaiWai Thin")
        print ("success 06")
        time.sleep(2)

        #Check email value is matched or not
        email = self.driver.find_element(By.NAME,"email")
        print ("success 07")
        val = email.get_attribute("value")
        print ("success 08")
        if val == rue : print("Email Matches")
        else : print("Email does not match")

        #I identify as
        time.sleep(3)
        print ("success 09")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/span").click()
        time.sleep(3)
        print ("success 10")


        #Home Country
        self.driver.find_element(By.CLASS_NAME, "css-o38cm9-control").click()
        #since this is from aws server, we need to select image src link to choose home country
        self.driver.find_element(By.XPATH, "//img[@src='https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png']").click()
        print("Success home country case")

        #Scroll to the country box
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        #Country
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[1]").click()
        time.sleep(2)
        print ("success 11")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input").send_keys("Myanmar")
        time.sleep(2)
        print ("success 12")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]/div[1]").click()
        time.sleep(2)
        print ("success 13")

        #Random Mobile Number
        fnum=[random.randint(0,9) for y in range(9)]
        random_mobile_number="".join(str(z) for z in fnum)
        self.driver.find_element(By.NAME, "mobile").send_keys(random_mobile_number)
        time.sleep(2)
        print ("success 14")

        #DOB
        self.driver.find_element(By.ID, "dob").click()
        time.sleep(2)
        print ("success 15")

        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[74]").click()
        time.sleep(2)
        Select(self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1998")
        time.sleep(2)
        print ("success 16")

        #month
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")
        time.sleep(2)
        print ("success 17")

        #day
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()
        time.sleep(2)
        print ("success 18")

        #Referral
        time.sleep(3)
        self.driver.find_element(By.NAME, "referral").send_keys(("X96695X2"))
        print("Enter referral code successfully")

        #Button click
        time.sleep((3))
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button").click()
        print("Go to next page successfully")
        time.sleep(5)

        #Click on name text box and clicked on 'Enter' key to show error message
        time.sleep(5)
        self.driver.find_element(By.NAME, "name").send_keys(Keys.RETURN)
        time.sleep(5)

        err_msg_name = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[1]/div[2]").text
        print(err_msg_name)
        time.sleep(5)

        err_msg_mobile = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[2]/div[2]").text
        print(err_msg_mobile)
        time.sleep(5)

        #Enter emergency contact name
        self.driver.find_element(By.NAME, "name").send_keys("QA Wai Wai")
        time.sleep(2)
        #Enter emergency contact number
        #Random Mobile Number
        sec_num=[random.randint(0,9) for y in range(9)]
        random_contact_number="".join(str(b) for b in sec_num)
        self.driver.find_element(By.NAME, "mobile").send_keys(random_contact_number)
        time.sleep(2)

        #Click on T&C checkbox
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[2]/div/label/div/div").click()
        time.sleep(2)

        #Register btn Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/button").click()
        print("Go to next page (OTP screen)  successfully")
        time.sleep(10)

    def test_login_after_registration_success(self):
        #Click on SignIn button
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[2]/a").click()
        time.sleep(3)

        #Checking Login form validations
        self.driver.find_element(By.NAME, "email").send_keys(Keys.ENTER)
        time.sleep(2)
        email_err="Email address is required"
        pwd_err="Password is required"
        act_email_err=self.driver.find_element(By.XPATH,"/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/label[1]/div[2]/div").text
        time.sleep(2)
        act_pwd_err=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/label[2]/div[2]/div").text
        time.sleep(2)

        if email_err==act_email_err and pwd_err==act_pwd_err:
            print("Login form's required validation testing success!!")
        else:
            print("Login form's required validation testing failed!!")

    #Checking invalid email, incorrect pwd and mail validations

        self.driver.find_element(By.NAME, "email").send_keys("waiwai@11")
        time.sleep(2)
        exp_err_msg="Invalid email address"
        act_err_msg=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/label[1]/div[2]/div").text
        print(act_err_msg)
        if exp_err_msg==act_err_msg:print("Mail validation is successful!!")
        else:print("Mail validation is failed!!")
        time.sleep(5)
        email_element= self.driver.find_element(By.NAME, "email")
        pwd_element= self.driver.find_element(By.NAME, "password")
        time.sleep(5)

#Clear back input fields

        email_element.send_keys(Keys.COMMAND + "a")  # Select all
        email_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

        pwd_element.send_keys(Keys.COMMAND + "a")  # Select all
        pwd_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

        # self.driver.execute_script("arguments[0].removeAttribute('readonly')", email_element)
        # self.driver.execute_script("arguments[0].removeAttribute('disabled')", email_element)
        # email_element.click()
        # time.sleep(2)
        # email_element.clear()
        # time.sleep(2)
        # self.driver.execute_script("arguments[0].removeAttribute('readonly')", pwd_element)
        # self.driver.execute_script("arguments[0].removeAttribute('disabled')", pwd_element)
        # pwd_element.click()
        # time.sleep(2)
        # pwd_element.clear()
        # time.sleep(2)
        #
        # self.driver.execute_script("arguments[0].value = '';", email_element)
        # time.sleep(2)
        # self.driver.execute_script("arguments[0].value = '';", pwd_element)
        # time.sleep(2)
        #
        # email_element.click()
        # time.sleep(2)
        # email_element.clear()
        # time.sleep(5)
        #
        # pwd_element.click()
        # time.sleep(2)
        # pwd_element.clear()
        # time.sleep(5)

        print("Hello waiwai")

        self.driver.find_element(By.NAME, "email").send_keys("aung10@yopmail.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys("P@ssw0rd34523twer", Keys.RETURN)
        print("Added invalid pw")
        time.sleep(5)
        #print("Before clicked SignIn button")
        #self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button/div").click()
        #self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
        #time.sleep(5)
        #print("I Clicked on SignIn button")

        exp_val_msg="The email address or password is not correct. Please try again."
        act_val_msg=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div[1]/div").text
        if exp_val_msg==act_val_msg:print("Account validation is successful!!")
        else:print("Account validation is failed!!")
        time.sleep(2)

        #Clear back input fields

        email_element.send_keys(Keys.COMMAND + "a")  # Select all
        email_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

        pwd_element.send_keys(Keys.COMMAND + "a")  # Select all
        pwd_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

        self.driver.find_element(By.NAME, "email").send_keys("ag@yopmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("P@ssw0rd", Keys.RETURN)
        #self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button/div").click()
        time.sleep(5)

        exp_m_val_msg="Invalid email and password"
        act_m_val_msg=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div[1]/div").text
        if exp_m_val_msg==act_m_val_msg:print("Incorrect email validation is successful!!")
        else:print("Incorrect email validation is failed!!")
        time.sleep(2)

        #Clear back input fields

        email_element.send_keys(Keys.COMMAND + "a")  # Select all
        email_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

        pwd_element.send_keys(Keys.COMMAND + "a")  # Select all
        pwd_element.send_keys(Keys.DELETE)  # Press Delete key
        time.sleep(2)

    #Login with correct credentials

        self.driver.find_element(By.NAME, "email").send_keys("aung10@yopmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("P@ssw0rd", Keys.RETURN)
        #self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button/div").click()
        time.sleep(5)

    #Check Login success or not
        exp_title="LOOKS LIKE YOU’RE IN SINGAPORE!"

        act_title=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/h2").text
        if (act_title):
            print(act_title)
            if exp_title==act_title:
                print("Country location checking is successful!!")
            else:print("Country location validation is failed!!")
            self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
            time.sleep(2)

        else: print("Your are in Myanmar so, we cannot continue")

        exp_welcome_txt=self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a/span").text
        print(exp_welcome_txt)
        time.sleep(3)

        if exp_welcome_txt.startswith("HI"): print("Login Successful!!")
        else:print("Login Failed!!")

    def test_clicking_multi_contents(self):
        print(f"Original tab URL: {self.driver.current_url}")

# Find all the links that open new tabs
        links = self.driver.find_elements("xpath", "//*[starts-with(@class, 'homeBanner')]")  # Replace with the actual locator

# Store the original tab handle
        original_tab = self.driver.current_window_handle

# Iterate through each link
#         •	The enumerate function adds a counter to an iterable (like a list).
#         •	It returns an iterator that produces tuples. Each tuple contains:
#         •	The index (starting at 0 by default, unless specified otherwise).
#         •	The value of the corresponding item in the iterable.
        for index, link in enumerate(links):
    # Click on the link
            link.click()
            time.sleep(2)  # Wait for the new tab to open

    # Get all window handles
            window_handles = self.driver.window_handles

    # Switch to the last opened tab
            self.driver.switch_to.window(window_handles[-1])

    # Get and print the URL of the new tab
            print(f"Tab {index + 1} URL: {self.driver.current_url}")

    # Perform any actions on the new tab if needed

    # Switch back to the original tab
            self.driver.switch_to.window(original_tab)

# Confirm we are back in the original tab
            print(f"Back to original tab URL: {self.driver.current_url}")

    def test_adding_new_fri_at_YMLife_Page(self):
        #element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/main/div[2]/div/div[1]/section/div[3]")
        #driver.execute_script("arguments[0].scrollIntoView();", element)
        #time.sleep(2)

#Adding new friend
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/main/div[1]/section/div[2]/div[1]").click()
        time.sleep(2)
        print("Clicked to add fri")
        input_for_fri_email=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/form/label/input")
        time.sleep(2)

    #Invalid email added case
        input_for_fri_email.send_keys("aunfasd@yol.cm")
        input_for_fri_email.send_keys(Keys.RETURN)
        time.sleep(2)
        invalid_fri_list=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/ul/li/section/div/p").text
        print(invalid_fri_list)
        time.sleep(2)
        #Clear textbox data
        self.driver.find_element(By.XPATH, "//img[@src='https://webfront-uat.yogamovement.com/img/icons/input-close.svg']" ).click()
        time.sleep(2)

    #Valid and new fri email added case
        input_for_fri_email.send_keys("aung4@yopmail.com")
        input_for_fri_email.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='https://webfront-uat.yogamovement.com/img/icons/add.svg']" ).click()
        time.sleep(2)
        req_text=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/ul/div[2]/div[3]/div").text
        if req_text=='REQUESTED': print("Email requested successfully!!")
        else:print("Email request failed!!")
        time.sleep(2)
        #Clear textbox data
        self.driver.find_element(By.XPATH, "//img[@src='https://webfront-uat.yogamovement.com/img/icons/input-close.svg']" ).click()
        time.sleep(2)

    #Valid but already sent email added case
        input_for_fri_email.send_keys("aung1@yopmail.com")
        input_for_fri_email.send_keys(Keys.RETURN)
        time.sleep(2)
        ag1_requested_txt=self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/ul/div/div[3]/div").text
        if ag1_requested_txt == 'REQUESTED': print("This email is already requested. Plz try with new one!!")
        time.sleep(2)
        #Clear textbox data
        self.driver.find_element(By.XPATH, "//img[@src='https://webfront-uat.yogamovement.com/img/icons/input-close.svg']" ).click()
        time.sleep(2)

    def test_remove_fri(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/main/div[1]/section/div[2]/div[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='https://webfront-uat.yogamovement.com/img/icons/remove.svg']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/div/div/ul/div[1]/div[3]/div/button[2]").click()
        time.sleep(2)

    def test_edit_profile(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a/span/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[1]/nav/ul/li[12]/a/div").click()
        time.sleep(5)

        element = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div/main/form/div[2]/div[2]/div[2]/label/div")  # Replace with your element's ID or selector
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)

        self.driver.find_element(By.CLASS_NAME, "css-tlfecz-indicatorContainer").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]').click()
        time.sleep(3)

        self.driver.find_element(By.NAME, "note_instructor").clear()
        time.sleep(3)
        self.driver.find_element(By.NAME, "note_instructor").send_keys("This note is updated by waiwai")
        time.sleep(2)

        self.driver.find_element(By.NAME, "emergency_contact_name").clear()
        time.sleep(3)
        self.driver.find_element(By.NAME, "emergency_contact_name").send_keys("Daw THW is updated new contact")
        time.sleep(2)

        self.driver.find_element(By.NAME, "emergency_contact_no").clear()
        time.sleep(3)
        self.driver.find_element(By.NAME, "emergency_contact_no").send_keys("688916061")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div/main/form/div[5]/button/div").click()
        time.sleep(3)

        Success_Msg=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div/main/div[2]/div/div[2]").text
        print(Success_Msg)

    def test_buy_class_pack(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[2]/a[2]/div/button[1]").click()
        time.sleep(2)

        print("Before clicking on All access menu")
        self.driver.find_element(By.LINK_TEXT, "ALL ACCESS").click()
        time.sleep(2)
        print("After clicking on All access menu")

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]").click()
        print("After clicking unknown button")

    # All Access btn Click
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]/div[4]/button").click()
        time.sleep(2)
    #Next Btn
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button").click()
        print("Test 3:", "All Class Success")

    def test_summary(self):
        print(1)
        img_path = "/Users/aungwaiwaithin/Downloads/Payment change.png"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/label/input").send_keys(img_path)
        print("Image Success!")

    def test_payment_method(self):
        time.sleep(2)
    #Change Button *** (This is special code)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/button").click()
        time.sleep(3)

        js_code = """let element = document.querySelector("input[name='hidden']");
                        element.disable = false;
                        return element"""
    #Car Number *** (This is special code)
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure card number input frame']")
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "cardnumber").send_keys("4111111111111111")
        self.driver.switch_to.default_content()
        time.sleep(3)

    #exp-date

        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure expiration date input frame']")
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "exp-date").send_keys("12/26")
        self.driver.switch_to.default_content()

    #CVC
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure CVC input frame']")
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.switch_to.default_content()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/button").click()
        time.sleep(3)
        file_path = "Payment change.png"
        self.driver.save_screenshot(file_path)
        print("Payment Success")

    def test_main(self):
        self.test_open_browser()
        time.sleep(3)
        #self.test_register_test()
        self.test_login_after_registration_success()
        time.sleep(5)
        #self.test_clicking_multi_contents()
        #time.sleep(3)
        #self.test_adding_new_fri_at_YMLife_Page()
        #time.sleep(3)
        #self.test_remove_fri()
        #time.sleep(3)
        #self.test_edit_profile()
        #time.sleep(5)
        self.test_buy_class_pack()
        time.sleep(5)
        self.test_summary()
        time.sleep(5)
        self.test_payment_method()
        time.sleep(5)

TestYoGa().test_main()

# self.driver.find_element(By.XPATH, "//img[@src='https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png']").click()

#Different types of scrolling behaviors
# 1. Scroll down by a specific pixel value
#driver.execute_script("window.scrollBy(0, 500);")
#time.sleep(2)

# 2. Scroll to the bottom of the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(2)

# 3. Scroll back to the top of the page
#driver.execute_script("window.scrollTo(0, 0);")
#time.sleep(2)

# 4. Scroll to a specific element
#element = driver.find_element(By.ID, "element-id")  # Replace with your element's ID or selector
#driver.execute_script("arguments[0].scrollIntoView();", element)
#time.sleep(2)

# 5. Use ActionChains to scroll (alternative)
#from selenium.webdriver.common.action_chains import ActionChains
#actions = ActionChains(driver)
#actions.send_keys(Keys.PAGE_DOWN).perform()
#time.sleep(2)