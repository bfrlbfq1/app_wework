'''
主页面
'''
import allure
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.contactlistpage import ContactListPage


class MainPage(BasePage):
    '''进入通讯录'''

    def goto_contactlist(self):
        with allure.step('进入通讯录'):
            locator=(MobileBy.XPATH, '//*[@text="通讯录"]')
            self.find_click(locator)
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return ContactListPage(self.driver)
