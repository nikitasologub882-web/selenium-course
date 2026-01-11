import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Инициализация сервиса и драйвера Chrome
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие главной страницы FreeConferenceCall
driver.get("https://www.freeconferencecall.com/")
time.sleep(3)  # Ожидание полной загрузки страницы

# Поиск и клик по кнопке "Login" (Войти)
login_button = driver.find_element("xpath", "//a[@class='me-1 btn btn-light']")
login_button.click()
time.sleep(2)  # Даем время для загрузки формы

# Поиск поля ввода email и ввод значения
email_field = driver.find_element("xpath", "//input[@id='login_email']")
# ввод текста в поле ввода
email_field.send_keys("nikitasologub30@mail.ru")
#print(email_field.get_attribute("value"))
time.sleep(2)
email_field.clear()# очистить поле ввода
email_field.send_keys("АААА")# изменение текста почты
time.sleep(10)  # Ожидание для визуальной проверки

