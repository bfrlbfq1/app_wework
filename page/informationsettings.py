from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.editmemberspage import EditMembersPage

"""
个人信息设置页
"""
class InformationSettings(BasePage):
    def information_settings(self):
        self.fing(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return EditMembersPage(self.driver)