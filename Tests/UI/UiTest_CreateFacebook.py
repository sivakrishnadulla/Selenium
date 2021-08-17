from PageActions.CommonFunctions import Commonfunctions
from PageObjects.createFacebook_locators import FacebookLogin
import time
import yaml


with open('../TestData/f_cratecred.yaml', 'r') as file:
    f_cratecreds = yaml.full_load(file)

cMethods = Commonfunctions()
f_objects = FacebookLogin()

cMethods.open_url('https://en-gb.facebook.com/')
time.sleep(5)
cMethods.maximize_window()
time.sleep(2)
cMethods.click_on_button(f_objects.createnew_xpath)
time.sleep(2)
cMethods.click_on_inputs_for_send_keys(f_objects.fname_xpath, f_cratecreds['firstname'])
cMethods.click_on_inputs_for_send_keys(f_objects.sname_xpath, f_cratecreds['surname'])
cMethods.click_on_inputs_for_send_keys(f_objects.mobile_xpath, f_cratecreds['mobileno'])
cMethods.click_on_inputs_for_send_keys(f_objects.newpassword_xpath, f_cratecreds['password'])
cMethods.click_on_inputs_for_send_keys(f_objects.day_xpath, f_cratecreds['date'])
cMethods.click_on_inputs_for_send_keys(f_objects.month_xpath, f_cratecreds['month'])
cMethods.click_on_inputs_for_send_keys(f_objects.year_xpath, f_cratecreds['year'])
cMethods.click_on_button(f_objects.gender_xpath)
cMethods.click_on_button(f_objects.signup_btn_xpath)

time.sleep(5)

cMethods.close_browser()