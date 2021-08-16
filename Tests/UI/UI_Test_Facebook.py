from PageActions.CommonFunctions import Commonfunctions
from PageObjects.Facebook_ObjectLocator import FacebookLogin
from PageObjects.Facebook_ObjectLocator import FacebookPost
from PageObjects.Facebook_ObjectLocator import FacebookEvents
import time


import yaml

with open('../TestData/F_cred.yaml', 'r') as f_file:
    f_creds = yaml.load(f_file)

cMethods = Commonfunctions()
F_objects = FacebookLogin()
F_posts = FacebookPost()
F_events = FacebookEvents()


cMethods.open_url('https://www.facebook.com/')
time.sleep(2)

cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_inputs_for_send_keys(F_objects.username_xpath, f_creds['username'])
cMethods.click_on_inputs_for_send_keys(F_objects.password_xpath, f_creds['password'])
cMethods.click_on_button(F_objects.login_btn_xpath)
time.sleep(2)

cMethods.alerts_browser()

cMethods.click_on_inputs_for_send_keys(F_posts.post_text_xpath, "Hello All")
cMethods.click_on_button(F_posts.post_btn_xpath)

cMethods.click_on_button(F_events.notifications_xpath)
cMethods.click_on_button(F_events.messenger_xpath)
cMethods.click_on_button(F_events.dropdown_xpath)

