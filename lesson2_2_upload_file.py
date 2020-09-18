#selenium_env\Scripts\activate.bat
import os
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys('Ivan')
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys('Petrov')
    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys('azaza@mail.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Example.txt')
    browser.find_element_by_id("file").send_keys(file_path)
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()