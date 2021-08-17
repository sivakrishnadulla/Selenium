"""
Locators for different objects that are designated through classes
"""
class SignUp:
    """
    element locators or xpaths for signup objects and some checkboxes for days,
    and buttons for gender
    """
    frame_xpath = "//iframe"
    fname_txt_xpath = '//input[@name="RESULT_TextField-1"]'
    lname_txt_xpath = '//input[@name="RESULT_TextField-2"]'
    phone_txt_xpath = '//input[@name="RESULT_TextField-3"]'
    country_txt_xpath = '//input[@name="RESULT_TextField-4"]'
    city_txt_xpath = '//input[@name="RESULT_TextField-5"]'
    email_txt_xpath = '//input[@name="RESULT_TextField-6"]'

    gender_btn_xpath = '//label[@for="RESULT_RadioButton-7_0"]'

    monday_checkbox_xpath = '//label[@for="RESULT_CheckBox-8_1"]'
    tuesday_checkbox_xpath = '//label[@for="RESULT_CheckBox-8_2"]'
    friday_checkbox_xpath = '//label[@for="RESULT_CheckBox-8_5"]'

    choose_files_xpath = '//input[@id="RESULT_FileUpload-10"]'
    signup_submit_xpath = '//input[@id="FSsubmit"]'

class SearchEvents:
    """
    element locators or xpaths for calendar objects
    locator for alert button

    """
    searchbar_xpath = '//input[@id="Wikipedia1_wikipedia-search-input"]'
    searchbutton_xpath = '//input[@class="wikipedia-search-button"]'
    datepicker_xpath = '//input[@id="datepicker"]'
    prev_calender_xpath = '//a[@data-handler="prev"]'
    next_calender_xpath = '//a[@data-handler="next"]'
    Alert_btn_click_xpath = '//button[text()="Click Me"]'

class DropdownEvents:
    """
    locators for dropdown objects
    """
    speed_drpdown_xpath = '//select[@id="speed"]'
    files_drpdown_xpath = '//select[@id="files"]'
    number_drpdown_xpath = '//select[@name="number"]'
    products_drpdown_xpath = '//select[@name="products"]'
    animals_drpdown_xpath = '//select[@name="animals"]'
    besttime_timeto_contact_drpdown_xpath = '//select[@name="RESULT_RadioButton-9"]/option[@value="Radio-2"]'

class AdvancedEvents:
    """
    locators for double click objects, drag and drop objects, slider objects
    and resizable elements

    """
    doubleclickbox_txt_xpath = '//input[@id="field1"]'
    doubleclick_btn_xpath = '//button[text()="Copy Text"]'
    dragme_xpath = '//div[@id="draggable"]'
    drophere_xpath = '//div[@id="droppable"]'
    dragimg_xpath = '//h5[text()="Mary"]'
    droping_trash_xpath = '//div[@id="trash"]'
    slider_xpath = '//span[contains(@class,"ui-slider-handle")]'
    resizable_xpath = '//div[@class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se"]'
