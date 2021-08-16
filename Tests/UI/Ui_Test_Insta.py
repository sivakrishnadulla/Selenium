from PageActions.CommonFunctions import Commonfunctions
from PageObjects.Insta_ObjectLocator import InstagramLogin
from PageObjects.Insta_ObjectLocator import InstagramEvents
import time

import yaml

with open('../TestData/Insta_cred.yaml', 'r') as I_file:
    Insta_creds = yaml.full_load(I_file)

cMethods = Commonfunctions()
I_objects = InstagramLogin()
I_events = InstagramEvents()

cMethods.open_url('https://www.instagram.com/')
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_inputs_for_send_keys(I_objects.username_xpath, Insta_creds['username'])
cMethods.click_on_inputs_for_send_keys(I_objects.password_xpath, Insta_creds['password'])
cMethods.click_on_button(I_objects.login_btn_xpath)
cMethods.click_on_button(I_objects.notnow_popup_xpath)
time.sleep(3)
cMethods.click_on_button(I_objects.notnow_notifications_xpath)

cMethods.click_on_button(I_events.explore_xpath)
time.sleep(4)
cMethods.click_on_button(I_events.messages_xpath)
time.sleep(2)
cMethods.click_on_button(I_events.notifications_xpath)
time.sleep(4)
cMethods.click_on_inputs_for_send_keys(I_events.search_xpath, "python")
