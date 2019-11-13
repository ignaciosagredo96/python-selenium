import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common import Common


class FirstTest(unittest.TestCase):

    def test_first_selenium(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://10.235.29.86:9081/portalempresas/")
        Common.click(driver, "//button[contains(@class,'button button--pill')]")
        Common.sendKeysID(driver, "INP_COMMON_RUT_CLIENTRUT", "70.360.100-6")
        Common.sendKeysID(driver, "INP_COMMON_RUT_USERRUT", "20.628.711-K")
        Common.sendKeysID(driver, "INP_COMMON_PASSWORD_PASSWORD", "123456a")
        teststrs = driver.find_element_by_id("INP_COMMON_PASSWORD_PASSWORD").get_attribute("value")
        Common.clickId(driver, "BTN_COMMON_LOGIN")
        driver.implicitly_wait(5)
        driver.quit()
