from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBarPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
       super().__init__(driver)
       self.__selectLanguageButtonLocator = ()
       self.__cookieNumberLocator = (By.ID, "cookieNumbers")

    def click_the_Select_language_button(self):
        selectLanguageButton= self._find_element(self.__selectLanguageButtonLocator)
        self._click_to_element(selectLanguageButton)

    def click_to_cookie_number(self):
        cookieNumberElement = self._find_element(self.__cookieNumberLocator)
        self._click_to_element(cookieNumberElement)