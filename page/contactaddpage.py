import allure
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class ContactAddPage(BasePage):
    def set_name(self,name):
        with allure.step('进行添加成员'):
            # 输入姓名
            locator_name=(MobileBy.XPATH, "//*[@text='必填']")
            self.fing(locator_name).send_keys(name)
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(name)
        return self
    def set_gender(self,sex):
        # 选择性别
        locator_sex=(MobileBy.ID, "com.tencent.wework:id/e93")
        self.find_click(locator_sex)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e93").click()
        if sex == '男':
            print(sex)
            locator_man = (MobileBy.XPATH, "//*[@text='男']")
            # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
            self.find_click(locator_man)
            # self.driver.find_element(*locator).click()

        else:
            locator_woman=(MobileBy.XPATH, "//*[@text='女']")
            self.find_click(locator_woman)
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        return self
    def set_phonnum(self,phone):
        locator_phone=(MobileBy.XPATH, "//*[@text='手机号']")
        self.fing(locator_phone).send_keys(phone)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        return self
    def click_save(self):
        from page.addmemberpage import AddMemberPag
        # 保存
        locator_click=(MobileBy.ID, 'com.tencent.wework:id/hi9')
        self.find_click(locator_click)
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hi9').click()
        return AddMemberPag(self.driver)
