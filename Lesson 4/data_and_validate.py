"""
Этот скрипт автоматизирует тестирование веб-страницы Wikipedia с помощью Selenium.
Основные шаги:
1. Настройка и запуск Chrome через WebDriver
2. Открытие страницы Wikipedia
3. Проверка корректности URL и заголовка
4. Визуальная проверка с небольшой задержкой
"""

import time  # Для создания пауз: time.sleep(секунды)

from selenium import webdriver  # Главный модуль Selenium WebDriver

"""
webdriver_manager автоматически скачивает правильную версию ChromeDriver.
Это избавляет от ручной загрузки драйвера и обновлений.
"""
from webdriver_manager.chrome import ChromeDriverManager

"""
Service управляет процессом ChromeDriver:
- Запуск
- Остановка
- Настройка портов
- Логирование
"""
from selenium.webdriver.chrome.service import Service

"""
Создаём объект Service с автоматической установкой ChromeDriver.
ChromeDriverManager().install() делает:
1. Проверяет установленную версию Chrome
2. Ищет совместимый ChromeDriver
3. Скачивает, если нет локально
4. Возвращает путь к драйверу
"""
service = Service(executable_path=ChromeDriverManager().install())

"""
Создаём объект браузера Chrome.
driver - это наш "пульт управления" браузером.
Через него мы будем взаимодействовать со страницей.
"""
driver = webdriver.Chrome(service=service)

"""
Переходим на главную страницу Wikipedia.
Примечание: Wikipedia делает редирект с wikipedia.org на www.wikipedia.org
"""
driver.get("https://wikipedia.org/")

"""
Проверяем, куда нас фактически перенаправили.
После get() страница загружается, могут работать скрипты перенаправления.
"""
url = driver.current_url
print("URL is", url)  # Для отладки и понимания текущего состояния

"""
Assert проверяет условие и останавливает выполнение при неудаче.
Важно: используется == (сравнение), а не = (присваивание).
На практике лучше использовать более гибкие проверки,
так как URL может меняться (http/https, www, параметры).
"""
assert url == "https://www.wikipedia.org/"

"""
Заголовок страницы (тег <title>) важен для SEO и пользователей.
В данном случае проверяем, что заголовок точь-в-точь "Wikipedia".
"""
current_title = driver.title
print("Текущий заголовок", current_title)
assert current_title == "Wikipedia"

# print(driver.page_source) # Печатаем HTML-код в терминал

time.sleep(3)




