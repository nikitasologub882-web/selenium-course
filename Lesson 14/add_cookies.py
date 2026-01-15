import time
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

# добавить собственную куку
driver.add_cookie({
    'name': 'Example',
    'value': 'Kukushka'
})
time.sleep(10)

# получить куку
print(driver.get_cookie("Example"))


