# encoding:utf-8
from lettuce import *
from appium import webdriver


@before.each_scenario
def lauchApp(scenario):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '192.168.83.101:5555'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    desired_caps['unicodeKeyboard'] = 'true'
    desired_caps['resetKeyboard'] = 'true'
    world.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


@after.each_scenario
def closeApp(scenario):
    world.driver.quit()


@step("I have two number:(\d+) and (\d+)")
def have2number(step, number1, number2):
    world.number1 = number1
    world.number2 = number2


@step("Do add method")
def doAdd(step):
    numa = world.driver.find_element_by_id("digit_" + world.number1)
    numa.click()

    add = world.driver.find_element_by_id("op_add")
    add.click()

    numb = world.driver.find_element_by_id("digit_" + world.number2)
    numb.click()

    equal = world.driver.find_element_by_id("eq")
    equal.click()

    world.result = world.driver.find_element_by_class_name("android.widget.EditText").text


@step("I get result:(\d+)")
def judgeResult(step, result):
    assert result == world.result, "The result are not equal %s and %s" % result and world.result
