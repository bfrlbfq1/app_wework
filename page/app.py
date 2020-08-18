from appium import webdriver

from page.basepage import BasePage
from page.mainpage import MainPage


class App(BasePage):
    def start(self):
        '''启动'''
        if  self.driver==None:
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
        else:
            self.driver.launch_app()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap_des)
        self.driver.implicitly_wait(20)
        return self

    def restart(self):
        '''重启'''
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        '''停止'''
        self.driver.quit()

    def goto_main(self):
        '''进入首页'''
        return MainPage(self.driver)
