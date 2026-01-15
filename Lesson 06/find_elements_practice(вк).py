from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com/id119973040")

time.sleep(3)

# отобразить количество одинаковых элементов
# print(len(driver.find_elements("class name","LeftMenu__itemLabel")))

# кликнуть нужный элемент по индексу
driver.find_elements("class name","LeftMenu__itemLabel")[2].click()

time.sleep(5)

