'''
手动添加页
'''
import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from page.basepage import BasePage
from page.contactaddpage import ContactAddPage


class AddMemberPag(BasePage):
    def add_menual(self):
        with allure.step('点击手动输入添加'):
            loctar=(MobileBy.ID, 'com.tencent.wework:id/cfu')
            self.find_click(loctar)
            # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/cfu').click()
        return ContactAddPage(self.driver)
    def get_toast(self):
        locator_toast=(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        element =self.fing_wait(locator_toast)
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        result = element.text
        return result