'''
通讯录页面
'''
import allure
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class ContactListPage(BasePage):

    def addcontact(self):
        from page.addmemberpage import AddMemberPag
        with allure.step('点击添加成员'):
            text ='添加成员'
            self.fing_roll(text)
        return AddMemberPag(self.driver)
    def search_contact(self):
        pass