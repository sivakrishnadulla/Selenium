from PageActions.CommonFunctions import Commonfunctions
import time

cMethods = Commonfunctions()

cMethods.open_url("https://the-internet.herokuapp.com/windows")
time.sleep(5)
cMethods.maximize_window()
time.sleep(2)
print(cMethods.get_page_title())

clickhere_xpath = '//a[@href="/windows/new"]'

cMethods.click_on_button(clickhere_xpath)
cMethods.click_on_button(clickhere_xpath)
cMethods.click_on_button(clickhere_xpath)
cMethods.click_on_button(clickhere_xpath)

cMethods.window_handler(1)
time.sleep(2)
cMethods.window_handler(2)
time.sleep(2)
cMethods.window_handler(4)
time.sleep(3)
cMethods.window_handler(3)

time.sleep(5)

cMethods.close_browser()