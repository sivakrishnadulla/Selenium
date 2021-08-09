from PageActions.CommonFunctions import Commonfunctions
from PageObjects.Insta_ObjectLocator import InstagramLogin
import time

import yaml

with open('TestData/Insta_cred.yaml', 'r') as I_file:
    I_creds = yaml.load(I_file)

cMethods = Commonfunctions()
I_objects = InstagramLogin()

cMethods.open_url('https://www.instagram.com/')
cMethods.maximize_browser()
time.sleep(3)

print(cMethods.get_page_title())


cMethods.click_on_inputs_for_send_keys(I_objects.username_xpath, I_creds['username'])
cMethods.click_on_inputs_for_send_keys(I_objects.password_xpath, I_creds['password'])
cMethods.click_on_button(I_objects.login_btn_xpath)
