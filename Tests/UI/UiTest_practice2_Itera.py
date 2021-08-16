from PageObjects.practice2_checkbox_Itera import CheckBox
from PageActions.CommonFunctions import Commonfunctions
import time

cMethods = Commonfunctions()
checkbox_objects = CheckBox()

cMethods.open_url("https://itera-qa.azurewebsites.net/home/automation")
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_button(checkbox_objects.gender_xpath)
cMethods.click_on_button(checkbox_objects.monday_xpath)
cMethods.click_on_button(checkbox_objects.friday_xpath)

time.sleep(5)
cMethods.close_browser()
