import time
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/")
time.sleep(3)


# Вернет куку name или любую другую указанную в качестве аргумента
# print (driver.get_cookie("country_code"))

print (driver.get_cookies()) #Вернет список словарей, все куки






