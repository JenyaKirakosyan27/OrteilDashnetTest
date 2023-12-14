from time import sleep
from pages_.navigationBarPage import NavigationBarPage

from tests_.baseTest import BaseTest


class ClicOnCookieTest(BaseTest):
    def test_clik_on_cookie(self):
        navigationBarObj = NavigationBarPage(self.driver)
        navigationBarObj.click_the_Select_language_button()
        sleep(10) #time is needed for the cookie button to activate
        navigationBarObj.click_to_big_cookie_button()
        sleep(10)



    def test_10000_clik_on_cookie(self):
        navigationBarObj = NavigationBarPage(self.driver)
        navigationBarObj.click_the_Select_language_button()
        sleep(10) #time is needed for the cookie button to activate
        navigationBarObj.click_to_several_times_cookie_button()
        sleep(10)


