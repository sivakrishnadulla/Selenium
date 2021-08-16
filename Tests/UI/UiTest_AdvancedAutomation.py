from PageActions.CommonFunctions import Commonfunctions
from PageObjects.signup_practice5_locators import AdvancedEvents, SearchEvents, DropdownEvents
from selenium.webdriver.common.by import By
import time
import yaml

with open('../TestData/Automation_signup_creds.yaml', 'r') as Automate_file:
    Automate_creds = yaml.full_load(Automate_file)

cMethods = Commonfunctions()
advanced_objects = AdvancedEvents()
search_objects = SearchEvents()
dropdown_objects = DropdownEvents()

cMethods.open_url("https://testautomationpractice.blogspot.com/?m=1")
time.sleep(5)
cMethods.maximize_window()

print(cMethods.get_page_title())

cMethods.browser.find_element(By.XPATH, advanced_objects.doubleclickbox_txt_xpath).clear()
cMethods.browser.find_element(By.XPATH, advanced_objects.doubleclickbox_txt_xpath).send_keys("SivaKrishna")
txt_box = cMethods.browser.find_element(By.XPATH, advanced_objects.doubleclick_btn_xpath)
cMethods.double_click(txt_box)
time.sleep(4)

source_drag = cMethods.browser.find_element(By.XPATH, advanced_objects.dragme_xpath)
target_drop = cMethods.browser.find_element(By.XPATH, advanced_objects.drophere_xpath)
cMethods.click_hold_move(source_drag, target_drop)
time.sleep(4)

source_img = cMethods.browser.find_element(By.XPATH, advanced_objects.dragimg_xpath)
target_img = cMethods.browser.find_element(By.XPATH, advanced_objects.droping_trash_xpath)
cMethods.drag_and_drop(source_img, target_img)
time.sleep(3)

slider_ele = cMethods.browser.find_element(By.XPATH, advanced_objects.slider_xpath)
cMethods.slider_element(slider_ele, 120, 0)
time.sleep(4)

resizeable_ele = cMethods.browser.find_element(By.XPATH, advanced_objects.resizable_xpath)
cMethods.scrollDown()
cMethods.scrollDown()
cMethods.move_element(resizeable_ele, 50, 5)

time.sleep(5)
cMethods.close_browser()

