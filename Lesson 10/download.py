# Загрузка и скачивание файлов

import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "downloads") # Универсальный путь для всех систем
}
chrome_options.add_experimental_option("prefs", preferences)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)
driver.find_elements("xpath", "//a")[3].click()
time.sleep(3)
