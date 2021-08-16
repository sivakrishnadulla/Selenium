from PageActions.CommonFunctions import Commonfunctions
from PageObjects.practice3_dropdown_locator import DropdownItera
import time

cMethods = Commonfunctions()
d_objects = DropdownItera()

cMethods.open_url('https://itera-qa.azurewebsites.net/home/automation')
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_button(d_objects.selectdropdown_xpath)
time.sleep(3)
cMethods.click_on_button(d_objects.value_dropdown_xpath)

time.sleep(5)

cMethods.close_browser()