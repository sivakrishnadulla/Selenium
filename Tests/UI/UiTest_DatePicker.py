from PageActions.CommonFunctions import Commonfunctions
from PageObjects.signup_practice5_locators import SearchEvents
from selenium.webdriver.common.by import By
import time

cMethods = Commonfunctions()
search_objects = SearchEvents()

cMethods.open_url("https://testautomationpractice.blogspot.com/?m=1")
time.sleep(5)
cMethods.maximize_window()

print(cMethods.get_page_title())

cMethods.click_on_inputs_for_send_keys(search_objects.searchbar_xpath, "python")
cMethods.click_on_button(search_objects.searchbutton_xpath)
time.sleep(3)

cMethods.click_on_button(search_objects.Alert_btn_click_xpath)
cMethods.alerts_browser_accept()
time.sleep(2)

cMethods.click_on_button(search_objects.datepicker_xpath)
month_year_title = cMethods.element_find(search_objects.datepicker_title_xpath)
dates_in_month = cMethods.elements_find(search_objects.no_of_dates_xpath)

for dateitem in dates_in_month:
    date = dateitem.text
    print(date, end=",")
    if date == '20':
        dateitem.click()
        break

print(month_year_title.text) #August 2021
month = month_year_title.split(" ")[0].strip()
year = month_year_title.split(" ")[1].strip()
#print(month)
#print(year)
# I want to pick 28-06-2020
while month == "June" and year == "2020":
    cMethods.click_on_button(search_objects.prev_calender_xpath)
    month_year_title = cMethods.browser.find_element(By.CLASS_NAME, "ui-datepicker-title").text
    print(month_year_title)
    month = month_year_title.split(" ")[0].strip()
    year = month_year_title.split(" ")[1].strip()

cMethods.browser.find_element(By.XPATH, '//a[text()="28"]')

time.sleep(3)

cMethods.close_browser()
