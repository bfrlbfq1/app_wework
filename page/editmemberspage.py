import allure
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


"""
编辑成员页面
"""
class EditMembersPage(BasePage):
    def edit_members_page(self):
        with allure.step('删除的成员'):
            text="删除成员"
            self.fing_roll(text)
            self.fing(MobileBy.XPATH, "//*[@text='确定']").click()
        from page.searchoinput import SearchInput
        return SearchInput(self.driver)