# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd

        wd.get("https://broex.xyz/")
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("login-email").clear()
        wd.find_element_by_id("login-email").send_keys("dev@broex.io")
        wd.find_element_by_id("login-password").clear()
        wd.find_element_by_id("login-password").send_keys("111")
        wd.find_element_by_id("login-email").click()
        wd.find_element_by_id("login-password").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_link_text("Assets").click()
        wd.find_element_by_link_text("Promotions").click()
        wd.find_element_by_link_text("Exchange").click()
        wd.find_element_by_link_text("Transactions").click()
        wd.find_element_by_link_text("Referral program").click()
        wd.find_element_by_link_text("Notifications").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notifications'])[1]/following::div[2]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Always'])[3]/following::*[name()='svg'][3]").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        time.sleep(5)
        self.wd.close()


if __name__ == "__main__":
    unittest.main()