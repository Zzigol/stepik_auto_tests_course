from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest 

def my_function(link):
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("Petrov555")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    return browser.find_element(By.TAG_NAME, "h1").text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"        
        self.assertEqual("Congratulations! You have successfully registered!", my_function(link), "Should be absolute value of a number")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"        
        self.assertEqual("Congratulations! You have successfully registered!", my_function(link), "Should be absolute value of a number")
if __name__ == "__main__":
    unittest.main()
