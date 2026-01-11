from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1) # явное ожидание

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTON = ("xpath","//button[text()='Remove']")

driver.find_element(*REMOVE_BUTTON).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))

print("Все ок")


