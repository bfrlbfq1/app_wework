'''
BasePage存放基础方法
'''
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def fing(self, locator):
        logging.info(f'driver.find_element(*locator)-->{locator}')
        return self.driver.find_element(*locator)

    def find_click(self, locator):
        logging.info(f"driver.find_element(*locator).click()-->{locator}")
        return self.driver.find_element(*locator).click()

    def fing_roll(self, text):
        logging.info(f'roll-->{text}')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable'
                                        '(new UiSelector().'
                                        'scrollable(true).'
                                        'instance(0)).'
                                        'scrollIntoView('
                                        'new UiSelector().'
                                        f'text({text}).instance(0));').click()

    def fing_wait(self, locator):
        logging.info(f'wait-->{locator}')
        return WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*locator))
