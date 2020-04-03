import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile


class Testnvbu(unittest.TestCase):

        def test_loginNVBU(self):
            self.driver = webdriver.Firefox("E:\software\geckodriver.exe")
            self.driver.maximize_window()
            self.driver.get("https://192.168.2.204:8443")
            self.driver.find_element_by_xpath("//input[@name='nvbu-login-username']").clear()
            self.driver.find_element_by_xpath("//input[@name='nvbu-login-username']").send_keys("admin")
            self.driver.find_element_by_xpath("//button[@id='quitemplate-appheader-button-login']").click()

        @classmethod
        def tearDown(cls):
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
