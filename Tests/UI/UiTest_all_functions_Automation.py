from PageActions.CommonFunctions import Commonfunctions
from PageObjects.signup_practice5_locators import AdvancedEvents, SearchEvents, DropdownEvents, SignUp
import time
import yaml

with open('../TestData/Automation_signup_creds.yaml', 'r') as Automate_file:
    Automate_creds = yaml.full_load(Automate_file)

cMethods = Commonfunctions()
advanced_objects = AdvancedEvents()
search_objects = SearchEvents()
dropdown_objects = DropdownEvents()
sign_objects = SignUp()
dd_objects = DropdownEvents()

cMethods.open_url("https://testautomationpractice.blogspot.com/?m=1")
time.sleep(5)
cMethods.maximize_window()

print(cMethods.get_page_title())

""" RIGHT SIDE ELEMENTS"""
cMethods.clear_field(advanced_objects.doubleclickbox_txt_xpath)
cMethods.click_on_inputs_for_send_keys(advanced_objects.doubleclickbox_txt_xpath, Automate_creds["keys"])
cMethods.double_click(advanced_objects.doubleclick_btn_xpath)
time.sleep(4)


source_drag = cMethods.element_find(advanced_objects.dragme_xpath)
target_drop = cMethods.element_find(advanced_objects.drophere_xpath)
#cMethods.click_hold_move(source_drag, target_drop)
time.sleep(4)

source_img = cMethods.element_find(advanced_objects.dragme_xpath)
target_img = cMethods.element_find(advanced_objects.droping_trash_xpath)
#cMethods.drag_and_drop(source_img, target_img)
time.sleep(3)

slider_ele = cMethods.element_find(advanced_objects.slider_xpath)
cMethods.slider_element(slider_ele, 120, 0)
time.sleep(4)

resizeable_ele = cMethods.element_find(advanced_objects.resizable_xpath)
cMethods.scrollDown()
cMethods.scrollDown()
cMethods.move_element(resizeable_ele, 50, 5)

cMethods.scrollUp()
time.sleep(3)
"""MIDDLE WEB ELEMENTS"""
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

"""LEFT SIDE ELEMENTS"""
cMethods.scrollUp()
cMethods.click_on_inputs_for_send_keys(search_objects.searchbar_xpath, "python")
cMethods.click_on_button(search_objects.searchbutton_xpath)
time.sleep(3)

cMethods.click_on_button(search_objects.Alert_btn_click_xpath)
cMethods.alerts_browser_accept()
time.sleep(2)

cMethods.click_on_button(search_objects.datepicker_xpath)
month_year_title = cMethods.element_find(search_objects.datepicker_title_xpath).text
dates_in_month = cMethods.element_find(search_objects.no_of_dates_xpath)

for dateitem in dates_in_month:
    date = dateitem.text
    print(date, end=",")
    if date == '20':
        dateitem.click()
        break

print(month_year_title) #August 2021

cMethods.click_on_inputs_for_send_keys(dd_objects.speed_drpdown_xpath, Automate_creds["speed"])
cMethods.click_on_inputs_for_send_keys(dd_objects.files_drpdown_xpath, Automate_creds["file"])
cMethods.click_on_inputs_for_send_keys(dd_objects.number_drpdown_xpath, Automate_creds["number"])
cMethods.click_on_inputs_for_send_keys(dd_objects.animals_drpdown_xpath, Automate_creds["animal"])
cMethods.click_on_inputs_for_send_keys(dd_objects.products_drpdown_xpath, Automate_creds["product"])

cMethods.click_on_button(sign_objects.signup_submit_xpath)

time.sleep(3)

time.sleep(5)
cMethods.close_browser()



