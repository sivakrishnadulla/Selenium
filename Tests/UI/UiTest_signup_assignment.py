from PageActions.CommonFunctions import Commonfunctions
from PageObjects.signup_practice5_locators import SignUp, DropdownEvents, SearchEvents
import time
import yaml

with open('../TestData/Automation_signup_creds.yaml', 'r') as Automate_file:
    Automate_creds = yaml.full_load(Automate_file)

cMethods = Commonfunctions()
sign_objects = SignUp()
dd_objects = DropdownEvents()
search_objects = SearchEvents()

cMethods.open_url("https://testautomationpractice.blogspot.com/?m=1")
cMethods.maximize_window()
time.sleep(5)

print(cMethods.get_page_title())

cMethods.switch_to_frame(sign_objects.frame_xpath)
cMethods.click_on_inputs_for_send_keys(sign_objects.fname_txt_xpath, Automate_creds["firstname"])
cMethods.click_on_inputs_for_send_keys(sign_objects.lname_txt_xpath, Automate_creds["lastname"])
cMethods.click_on_inputs_for_send_keys(sign_objects.phone_txt_xpath, Automate_creds["phone"])
cMethods.click_on_inputs_for_send_keys(sign_objects.country_txt_xpath, Automate_creds["country"])
cMethods.click_on_inputs_for_send_keys(sign_objects.city_txt_xpath, Automate_creds["city"])
cMethods.click_on_inputs_for_send_keys(sign_objects.email_txt_xpath, Automate_creds["mail"])

cMethods.click_on_button(sign_objects.gender_btn_xpath)
cMethods.scrollDown()
cMethods.click_on_button(sign_objects.monday_checkbox_xpath)
cMethods.click_on_button(sign_objects.tuesday_checkbox_xpath)
cMethods.click_on_button(sign_objects.friday_checkbox_xpath)

cMethods.click_on_button(dd_objects.besttime_timeto_contact_drpdown_xpath)

cMethods.click_on_inputs_for_send_keys(sign_objects.choose_files_xpath, 'F:\python files\selenium files\photos\ladakh_mountains.jpg')

#cMethods.scrollUp()
cMethods.click_on_inputs_for_send_keys(dd_objects.speed_drpdown_xpath, Automate_creds["speed"])
cMethods.click_on_inputs_for_send_keys(dd_objects.files_drpdown_xpath, Automate_creds["file"])
cMethods.click_on_inputs_for_send_keys(dd_objects.number_drpdown_xpath, Automate_creds["number"])
cMethods.click_on_inputs_for_send_keys(dd_objects.animals_drpdown_xpath, Automate_creds["animal"])
cMethods.click_on_inputs_for_send_keys(dd_objects.products_drpdown_xpath, Automate_creds["product"])

cMethods.click_on_button(sign_objects.signup_submit_xpath)a

time.sleep(3)
cMethods.close_browser()





