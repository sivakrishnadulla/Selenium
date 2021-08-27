"""
created a class for differents methods to use
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests

#from webdriver_manager.chrome import ChromeDriverManager
import time

class Commonfunctions:


    """
    A class that has all the functions that can do while testing
    """

    def __init__(self):

        """
        It is a instance of class. Declaring a variable using self instructor
        :return:
        """

        self.browser = webdriver.Chrome(r'C:\Users\lenovo\Selenium\AppDrivers\chromedriver.exe')

    def open_url(self, url):
        """
        To open any url we can use these method which has get method inside it
        :param url:
        :return:
        """
        self.browser.get(url)

    def maximize_window(self):
        """
        To Maximize the window we can use these method

        :return:
        """
        self.browser.maximize_window()

    def minimize_window(self):
        """

        :return: it will minimize the browser
        """
        self.browser.minimize_window()

    def get_page_title(self):
        """

        :return: to print the title of particular url we can use these method
        """
        return self.browser.title

    def click_on_inputs_for_send_keys(self, x_path, value):
        """

        :param x_path: it is used to perform click operation where the values has to be send
        :param value: give input as per requirement
        :return: these method will firstly click on xpath and then takes the inputs from value
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).send_keys(value)

    def click_on_button(self, x_path):
        """

        :param x_path: to click on particular object here xpath is used
        :return:
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).click()

    def alerts_browser_accept(self):
        """

        :return: when any alerts are occured these method will accept that alert and make automation continues
        """
        alert_object = self.browser.switch_to.alert
        alert_object.accept()

    def alerts_browser_dismiss(self):
        """

        :return:these method will dismiss the alert and continues automation
        """
        alert_obj = self.browser.switch_to.alert
        alert_obj.dismiss()

    def close_browser(self):
        """

        :return: it will completely close the browser
        """
        self.browser.close()

    def element_find(self, xpath):
        """

        :param xpath:
        :return:
        """
        self.browser.find_element(By.XPATH, xpath)

    def elements_find(self,  xpath):
        """

        :param xpath:
        :return:
        """
        self.browser.find_elements(By.XPATH, xpath)

    def move_element(self, xpath, x_offset, y_offset):
        """

        :param xpath: first object is gets clicked and holds by using xpath then moves in x-direction using
        x_offset and moves in y-direction using y_offset
        :return:it will release in that particular location after moving in x and y directions
        perform() will work as all these steps are done by perform method only
        """
        time.sleep(2)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(xpath).move_by_offset(x_offset, y_offset).release().perform()

    def scrollDown(self):
        """

        :return: it will scroll down the page
        """

        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()

    def scrollUp(self):
        """

        :return: it will scrollup the page
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()

    def drag_and_drop(self, source, target):
        """

        :param source: object that has to move from place to another place
        :param target: object where the source object will come and land
        :return: the source object will get dragged to target object
        """
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source, target).perform()

    def click_hold_move(self, source, target):
        """

        :param source: source object will get clicked and hold
        :param target: that source object will move to target element location
        :return: releases the source object into target location
        """

        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(source).move_to_element(target).release().perform()

    def window_handler(self, tab_number):
        """

        :param tab_number: number of tabs that wanted to be swithched. it is counted from left side
        :return: it will switch from one tab to different tab based on tab_number
        """
        change_window = self.browser.window_handles[tab_number]
        self.browser.switch_to.window(change_window)
    def clear_field(self, xpath):
        """

        :param xpath:
        :return:
        """
        self.browser.find_element(By.XPATH, xpath).clear()

    def double_click(self, xpath):
        """

        :param xpath: the object where the double click operation has to be done
        :return: it will click two times in the particular object or element
        """
        double = self.browser.find_element(By.XPATH, xpath)
        action_chains = ActionChains(self.browser)
        action_chains.double_click(double).perform()

    def slider_element(self, source, x_offset, y_offset):
        """

        :return: source object will get dragged and dropped in x and y directions
        in these case it is slider only in one direction it will get dragged
        """
        acions_chains = ActionChains(self.browser)
        acions_chains.drag_and_drop_by_offset(source, x_offset, y_offset).perform()

    def switch_to_frame(self, xpath):
        """
            This function will do -
                - switch the frame
        :return:
        """
        try:
            self.browser.switch_to.frame(self.browser.find_element_by_xpath(xpath))
        except NoSuchElementException:
            raise Exception("No element found")







