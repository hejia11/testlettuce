# encoding: utf-8
import sys

import unittest
from appium import webdriver
from ddt import ddt, data
import time


@ddt
class MyTestCase(unittest.TestCase):
    # 初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.83.101:5555'
        desired_caps['appPackage'] = 'com.android.browser'
        desired_caps['appActivity'] = 'com.android.browser.BrowserActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.base_url = "http://www.baidu.com"

    # 释放资源
    def tearDown(self):
        self.driver.quit()

    @data(u"java",u"python")
    def test_searchkeyword(self, keyword):
        self.driver.get(self.base_url)
        time.sleep(3)
        input1 = self.driver.find_elements_by_class_name("android.widget.EditText")
        print(input1[1])

        input1[1].send_keys(keyword)
        time.sleep(3)
        # self.driver.press_keycode(66)
        # self.driver.sendKeyEvent(66)
        button = self.driver.find_element_by_class_name("android.widget.Button")
        button.click()
        time.sleep(10)
        result0 = self.driver.find_elements_by_class_name("android.webkit.WebView")
        # result0 = self.driver.find_element_by_xpath('//*[@class="android.webkit.WebView" and @index="0"]')
        # result0 = self.driver.find_element_by_accessibility_id("java - 百度")
        print(result0)
        self.assertTrue(keyword in result0[0].get_attribute(name='content-desc'))

        '''for x in result0:
            print(x.id)
            print(x.get_attribute(name='content-desc') + "====")
            #self.assertTrue(keyword in x.get_attribute(name='content-desc'))'''


if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTest(cases)
    myTestRunner = unittest.TextTestRunner(verbosity=2)
    myTestRunner.run(suite)

print(sys.path)
