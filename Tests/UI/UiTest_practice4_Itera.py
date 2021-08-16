from PageActions.CommonFunctions import Commonfunctions
from PageObjects.practice4_itera_locators import RadioButton
import time

cMethods = Commonfunctions()
R_objects = RadioButton()

cMethods.open_url('https://itera-qa.azurewebsites.net/home/automation')
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_button(R_objects.xpath_2year)
time.sleep(3)
cMethods.click_on_button(R_objects.selenium_Rbtn_xpath)
cMethods.click_on_button(R_objects.testng_Rbtn_xpath)

time.sleep(3)
cMethods.close_browser()
