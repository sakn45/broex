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

        wd.get("https://broex.dev/")
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("login-email").clear()
        wd.find_element_by_id("login-email").send_keys("fedyano@gmail.com")
        wd.find_element_by_id("login-password").clear()
        wd.find_element_by_id("login-password").send_keys("Pn7ZrW244")
        wd.find_element_by_id("login-email").click()
        wd.find_element_by_id("login-password").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()


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
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()