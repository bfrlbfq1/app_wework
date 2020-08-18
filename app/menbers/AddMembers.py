'''
    添加成员页面
    1.实现添加成员测试需求
    2/实现删除成员测试需求
'''
import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import allure
import pytest
import yaml
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.feature('添加成员功能')
class TestMembers:
    logging.basicConfig(level=logging.INFO)
    with open('../../data/data.yaml', encoding='UTF-8') as f:
        data = yaml.safe_load(f)

    def setup(self):
        cap_des = {
            'platformName': 'android',
            # 'deviceName': '04157df40bf53115',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': 'true',
            'skipServerInstallation': 'true',
            'skipDeviceInitialization': 'true',
            'automationName': 'uiautomator2',
            'settings[waitForIdleTimeout]': 0

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap_des)
        self.driver.implicitly_wait(50)

    def teardown(self):
        self.driver.quit()
    # def setup(self):
    #     print('用例开始')
    # def teardown(self):
    #     self.driver.find_element(MobileBy.ID,'hhr').click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="消息"]').click()
    @allure.story('新增成员')
    @pytest.mark.parametrize('name,sex,phone_no', data)
    def test_add_member(self, name, sex, phone_no):
        '''添加成员'''
        with allure.step('进入通讯录'):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        with allure.step('点击添加成员'):
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable'
                                     '(new UiSelector().'
                                     'scrollable(true).'
                                     'instance(0)).'
                                     'scrollIntoView('
                                     'new UiSelector().'
                                     'text("添加成员").instance(0));').click()

        with allure.step('点击手动输入添加'):
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/cgl').click()
        with allure.step('进行添加成员'):
            # 输入姓名
            self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(name)
            # 选择性别
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b0j").click()
            if sex == '男':
                print(sex)
                locator = (MobileBy.XPATH, "//*[@text='男']")
                # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
                self.driver.find_element(*locator).click()

            else:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            # 输入手机号
            self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_no)
            # 保存
            self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
            # self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
            # 验证验证toast提示"添加成功"
            element = WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
            result = element.text
            assert "添加成功" in result

    with open('../../data/delData.yaml', encoding='UTF-8') as f:
        del_data = yaml.safe_load(f)

    @allure.story('删除成员')
    @pytest.mark.parametrize('name', del_data)
    def test_delmembers(self, name):
        '''散出成员'''
        with allure.step('进入通讯录'):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        with allure.step('搜索'):
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hk9').click()
        with allure.step('输入要删除的成员'):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        time.sleep(3)
        with allure.step('选择删除的成员'):
            elements_list = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        print(len(elements_list))
        logging.info('删除成员之前:'+str(len(elements_list)))
        if len(elements_list) < 2:
            print('没有这个联系人')
            return

        elements_list[1].click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hjz').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        with allure.step('删除的成员'):
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable'
                                     '(new UiSelector().'
                                     'scrollable(true).'
                                     'instance(0)).'
                                     'scrollIntoView('
                                     'new UiSelector().'
                                     'text("删除成员").instance(0));').click()

            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        with allure.step('验证是否删除成功'):
            time.sleep(2)
            elements_list_after = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
            logging.info('删除成员之后:' + str(len(elements_list_after)))
            sub=len(elements_list) - len(elements_list_after)
            assert sub == 1
