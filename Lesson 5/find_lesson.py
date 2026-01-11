
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ok.ru/")

time.sleep(3)

driver.find_element("class name","vkuiButton__in").click()

time.sleep(5)

# －Способы поиска эквивалентные By.***:
# ➖ ID = "id"
# ➖ XPATH = "xpath"
# ➖ NAME = "name"
# ➖ CLASS_NAME = "class name"
# ➖ CSS_SELECTOR = "css selector"