import unittest

from selenium import webdriver


class Common:
    @staticmethod
    def click(driver, xpath):
        element = driver.find_element_by_xpath(xpath)
        element.click()

    @staticmethod
    def sendKeys(driver, xpath, text):
        element = driver.find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def sendKeysID(driver, id, text):
        element = driver.find_element_by_id(id)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def clickId(driver, id):
        element = driver.find_element_by_id(id)
        element.click()