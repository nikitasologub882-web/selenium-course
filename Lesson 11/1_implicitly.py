# Явные и неявные ожидания

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5) # неявное ожидание
driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_5_SECOND_BUTTON = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*VISIBLE_AFTER_5_SECOND_BUTTON).click()
