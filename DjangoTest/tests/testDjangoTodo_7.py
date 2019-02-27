# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from VirtualWebDriver import VirtualWebDriver

class DjangoTODOListTestCase(unittest.TestCase):

    def login(self):
        self.driver.get("http://127.0.0.1:8000/admin")
        self.driver.find_element_by_id("id_username").click()
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").click()
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("1234abcd")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()

        print "login success\n"

    @classmethod
    def setUpClass(cls):
        print "setUpClass"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"


    def setUp(self):
        import pdb; pdb.set_trace()
        self.driver = VirtualWebDriver.getDriver()
        self.driver.implicitly_wait(30)
        self.login()

    def test01TaskList(self):
        self.driver.find_element_by_link_text("Items").click()
        self.driver.find_element_by_link_text("work 1").click()
        self.driver.find_element_by_link_text("Home").click()



    def test20UpdateTask(self):
        self.fail("testUpdateTask has not implemented\n") 


    def test30CreateTask(self):
        self.fail("testCreateTask has not implemented\n") 


    def test40DeleteTask(self):
        self.fail("testDeleteTask has not implemented\n")
   
    def tearDown(self):
        import pdb; pdb.set_trace()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
