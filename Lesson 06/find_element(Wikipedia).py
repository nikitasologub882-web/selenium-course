# Поиск веб - элементов.Часть 2

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# Найти иконку Wikipedia по имени класса
print(driver.find_element("class name","wikipedia-icon"))
time.sleep(3)

# Найти поле ввода Wikipedia по id
print(driver.find_element("id","Wikipedia1_wikipedia-search-input"))
time.sleep(3)

# Найти кнопку поиска Wikipedia по классу
print(driver.find_element("class name","wikipedia-search-button"))
time.sleep(3)

# Найти любой другой элемент на странице по тегу
print(driver.find_element("tag name","h1"))
time.sleep(3)

# Список тегов для поиска
#tags_to_find = ['h1', 'h2', 'h3', 'h4', 'p', 'a', 'input', 'button', 'img', 'table', 'div', 'span']