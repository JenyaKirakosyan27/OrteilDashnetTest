from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBarPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__selectLanguageButtonRuLocator = (By.ID, "langSelect-RU")
        self.__bigCookieNumberLocator = (By.ID, "bigCookie")

    def click_the_Select_language_button(self):
        selectLanguageButtonRuElement = self._find_element(self.__selectLanguageButtonRuLocator)
        self._click_to_element(selectLanguageButtonRuElement)

    def click_to_big_cookie_button(self):
        bigCookieButtonElement = self._find_element(self.__bigCookieNumberLocator)
        self._click_to_element(bigCookieButtonElement)


    # def click_to_times_cookie_button(self):
    #     bigCookieButtonElement = self._find_element(self.__bigCookieNumberLocator)
    #     self._click_to_element(bigCookieButtonElement)
    #