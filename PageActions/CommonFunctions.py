"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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

        :return:
        """
        self.browser.minimize_window()

    def get_page_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs_for_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).send_keys(value)

    def click_on_button(self, x_path):
        """

        :param x_path:
        :return:
        """
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).click()

    def alerts_browser_accept(self):
        """

        :return:
        """
        alert_object = self.browser.switch_to.alert
        alert_object.accept()

    def alerts_browser_dismiss(self):
        """

        :return:
        """
        alert_obj = self.browser.switch_to.alert
        alert_obj.dismiss()

    def close_browser(self):
        """

        :return:
        """
        self.browser.close()

    def move_element(self, xpath, x_offset, y_offset):
        """

        :param xpath:
        :return:
        """
        time.sleep(2)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(xpath).move_by_offset(x_offset, y_offset).release().perform()

    def scrollDown(self):
        """

        :return:
        """

        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()

    def scrollUp(self):
        """

        :return:
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()

    def drag_and_drop(self, source, target):
        """

        :param xpath:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source, target).perform()

    def click_hold_move(self, source, target):
        """

        :param source:
        :param target:
        :return:
        """

        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(source).move_to_element(target).release().perform()

    def change_window_tab(self, tab_number):
        """

        :param tab_number:
        :return:
        """
        change_window = self.browser.window_handles[tab_number]
        self.browser.switch_to.window(change_window)

    def double_click(self, xpath):
        """

        :param xpath:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.double_click(xpath).perform()

    def slider_element(self, source, x_offset, y_offset):
        """

        :return:
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

    def window_handler(self, arg):
        """

        :param arg:
        :return:
        """
        self.browser.window_handles
        change_window = self.browser.window_handles[arg]
        self.browser.switch_to.window(change_window)


