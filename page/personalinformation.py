from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.informationsettings import InformationSettings

"""
个人信息页
"""
class PersonalInformation(BasePage):
    def personal_information(self):
        self.fing(MobileBy.ID, 'com.tencent.wework:id/hjz').click()
        return InformationSettings(self.driver)
