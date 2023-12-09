
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math

try: 
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button1 = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1.click()
    
    browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = browser.find_element(By.ID, "input_value").text
#x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    
    button = browser.find_element(By.ID, "solve")
    button.click()       

finally:
    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    time.sleep(10)
    # закрываем браузер после всех манипул€ций
    browser.quit()

# не забываем оставить пустую строку в конце файла

