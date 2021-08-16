from PageObjects.SwagLabs_Locators import SignInSwagLabs, CartItems, Checkout
from PageActions.CommonFunctions import Commonfunctions
import time
import yaml

with open('../TestData/SwagLabs.yaml', 'r') as swag_file:
    swag_lab_file = yaml.full_load(swag_file)

cMethods = Commonfunctions()
sign_in_objects = SignInSwagLabs()
cart_objects = CartItems()
checkout_objects = Checkout()

cMethods.open_url("https://www.saucedemo.com/")
time.sleep(5)
cMethods.maximize_window()
time.sleep(3)

print(cMethods.get_page_title())

cMethods.click_on_inputs_for_send_keys(sign_in_objects.username_xpath, swag_lab_file["username"])
cMethods.click_on_inputs_for_send_keys(sign_in_objects.password_xpath, swag_lab_file["password"])
cMethods.click_on_button(sign_in_objects.login_btn_xpath)

cMethods.click_on_button(cart_objects.backpack_add_xpath)
cMethods.click_on_button(cart_objects.bikelight_add_xpath)
cMethods.click_on_button(cart_objects.jacket_add_xpath)

cMethods.click_on_button(cart_objects.cart_open_xpath)
time.sleep(3)

cMethods.click_on_button(checkout_objects.checkout_btn_xpath)
time.sleep(4)

cMethods.click_on_inputs_for_send_keys(checkout_objects.firstname_xpath, swag_lab_file["firstname"])
cMethods.click_on_inputs_for_send_keys(checkout_objects.lastname_xpath, swag_lab_file["lastname"])
cMethods.click_on_inputs_for_send_keys(checkout_objects.postal_code_xpath, swag_lab_file["postalcode"])
cMethods.click_on_button(checkout_objects.continue_btn_xpath)

cMethods.click_on_button(checkout_objects.finish_btn_xpath)

time.sleep(3)
cMethods.close_browser()
