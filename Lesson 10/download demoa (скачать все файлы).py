import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Создаем папку для загрузок
download_path = os.path.join("lesson_6", "downloads")
os.makedirs(download_path, exist_ok=True)

# Настройка браузера (как в примере)
chrome_options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": os.path.abspath(download_path)
}
chrome_options.add_experimental_option("prefs", preferences)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/download")
time.sleep(3)

# Находим все ссылки (как в примере, но все, а не только 4-ю)
all_links = driver.find_elements("xpath", "//a")

print(f"Найдено {len(all_links)} ссылок. Начинаю скачивание...")

# ЦИКЛ FOR для скачивания всех файлов
for i in range(len(all_links)):
    try:
        # Обновляем список ссылок на каждой итерации
        current_links = driver.find_elements("xpath", "//a")

        if i < len(current_links):
            # Кликаем по i-ой ссылке (как в примере [3].click())
            current_links[i].click()
            print(f"Скачиваю файл {i + 1} из {len(all_links)}")

            # Ждем загрузки (как в примере time.sleep(3))
            time.sleep(3)

    except Exception as e:
        print(f"Ошибка при скачивании файла {i + 1}: {e}")

print("\nВсе файлы скачаны!")
print(f"Проверьте папку: {os.path.abspath(download_path)}")


#Ключевые отличия от примера:
#Цикл for вместо конкретного индекса [3]
#Создана папка lesson_6/downloads
#Скачиваются ВСЕ файлы, а не только 4-й
#Добавлена обработка ошибок и логирование