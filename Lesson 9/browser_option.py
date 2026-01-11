# Импортируем модуль time для работы со временем
# Будем использовать для замера скорости загрузки страницы
import time

# Импортируем основной модуль Selenium WebDriver для автоматизации браузера
from selenium import webdriver

# Импортируем WebDriver Manager - утилиту для автоматического управления драйверами
# Она сама скачивает нужную версию ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем Service - класс для управления процессом ChromeDriver
from selenium.webdriver.chrome.service import Service

# Создаем объект ChromeOptions для настройки параметров запуска браузера Chrome
# Этот объект позволяет задавать различные опции и флаги командной строки
chrome_options = webdriver.ChromeOptions()

# Устанавливаем стратегию загрузки страницы в значение "normal"
# Это означает, что Selenium будет ждать полной загрузки страницы (всех ресурсов)
# Другие варианты: "eager" (ждет только DOM) или "none" (не ждет)
chrome_options.page_load_strategy = "normal"

# Включаем headless-режим (без графического интерфейса)
# Браузер работает в фоне, без открытия окна - полезно для серверов и CI/CD
chrome_options.add_argument("--headless")

# ЗАКОММЕНТИРОВАННЫЕ ОПЦИИ (можно активировать при необходимости):

# Режим инкогнито (приватный режим) - не сохраняет историю, куки и т.д.
# chrome_options.add_argument("--incognito")

# Игнорирование ошибок SSL-сертификатов
# Полезно при тестировании на локальных или тестовых серверах с самоподписанными сертификатами
# chrome_options.add_argument("--ignore-certificate-errors")

# Устанавливаем размер окна браузера 1920x1080 пикселей
# Важно для тестирования адаптивного дизайна и скриншотов
chrome_options.add_argument("--window-size=1920x1080")

# Попытка отключить кэш браузера (некорректный аргумент)
# Правильные варианты: "--disable-cache" или "--disk-cache-size=0"
# chrome_options.add_argument("--window-disable-cache")

# Создаем объект Service для управления ChromeDriver
# ChromeDriverManager().install() автоматически:
# 1. Проверяет текущую версию Chrome в системе
# 2. Скачивает совместимую версию ChromeDriver если она отсутствует
# 3. Возвращает путь к исполняемому файлу драйвера
service = Service(executable_path=ChromeDriverManager().install())

# Создаем экземпляр веб-драйвера для Chrome
# Передаем service (для управления процессом драйвера) и options (настройки браузера)
# Этот объект - основной инструмент для взаимодействия с браузером
driver = webdriver.Chrome(service=service, options=chrome_options)

# Фиксируем время начала выполнения операции (перед открытием страницы)
start_time = time.time()

# Метод get() открывает указанный URL в браузере
# В данном случае открываем сайт для проверки IP-адреса
driver.get("https://whatismyipaddress.com/")

# Фиксируем время после загрузки страницы
end_time = time.time()

# Вычисляем разницу между конечным и начальным временем
# Получаем время загрузки страницы в секундах
result = end_time - start_time

# Выводим результат в консоль
# Это покажет сколько времени заняла загрузка страницы от команды get() до полной загрузки
print(result)
