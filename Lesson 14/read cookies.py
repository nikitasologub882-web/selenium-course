import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Открываем страницу логина
driver.get("https://www.freeconferencecall.com/profile")

# Чистим все куки
driver.delete_all_cookies()

# Записываем куки из файла в переменную
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

# Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(2)

driver.refresh()

time.sleep(2)

