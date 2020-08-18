import logging
import time

import allure
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.personalinformation import PersonalInformation

"""
搜索页
"""
class SearchInput(BasePage):
    elements_list=None
    def search_input(self,name):
        with allure.step('输入要删除的成员'):
            self.fing(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        time.sleep(3)
        return self
    def click_del_value(self,name):
        with allure.step('选择删除的成员'):
            self.elements_list = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        print(len(self.elements_list))
        logging.info('删除成员之前:'+str(len(self.elements_list)))
        if len(self.elements_list) < 2:
            print('没有这个联系人')
            return

        self.elements_list[1].click()
        return PersonalInformation(self.driver)
    def assert_del(self,name):
        with allure.step('验证是否删除成功'):
            time.sleep(5)
            elements_list_after = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
            logging.info('删除成员之后:' + str(len(elements_list_after)))
            sub=len(elements_list_after)
            return sub