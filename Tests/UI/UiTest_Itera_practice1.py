from PageActions.CommonFunctions import Commonfunctions
from PageObjects.practice1_automtae_objectlocator import IteraSignUp
import time

import yaml

with open('../TestData/Itera_creds.yaml', 'r') as Itera_file:
    Iter_creds = yaml.load(Itera_file)

cMethods = Commonfunctions()
Itera_objects = IteraSignUp()

cMethods.open_url('https://itera-qa.azurewebsites.net/')
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_button(Itera_objects.signup_btn_xpath)

cMethods.click_on_inputs_for_send_keys(Itera_objects.fname_xpath, "SivaKrishna")
cMethods.click_on_inputs_for_send_keys(Itera_objects.Surname_xpath, "Dulla")
cMethods.click_on_inputs_for_send_keys(Itera_objects.E_post_xpath, "I love Travelling")
cMethods.click_on_inputs_for_send_keys(Itera_objects.Mobile_xpath, "6305667892")
cMethods.click_on_inputs_for_send_keys(Itera_objects.Username_xpath, Iter_creds["username"])
cMethods.click_on_inputs_for_send_keys(Itera_objects.password_xpath, Iter_creds["password"])
cMethods.click_on_inputs_for_send_keys(Itera_objects.confirm_password_xpath, Iter_creds["Confirmpassword"])

cMethods.click_on_button(Itera_objects.submit_btn_xpath)

time.sleep(5)

cMethods.close_browser()
