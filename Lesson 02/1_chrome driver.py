# Инициализация Chrome и Firefox драйверов

#импорт веб драйвера для взаимодействия с браузером
from selenium import webdriver

#импорт ChromeDriverManager для установки
from webdriver_manager.chrome import ChromeDriverManager

#импорт Service, который отвечает за установку, открытие и закрытие
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
