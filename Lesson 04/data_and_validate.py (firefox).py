from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
service = FirefoxService(executable_path='./geckodriver')  # укажите полный путь к вашему geckodriver
driver = webdriver.Firefox(service=service)

try:
    # Открываем первую страницу (например, VK)
    driver.get('https://vk.com/')

    # Получаем и выводим заголовок первой страницы
    print(f'Заголовок первой страницы: {driver.title}')

    # Открываем вторую страницу (например, Yandex)
    driver.get('https://ya.ru/')

    # Получаем и выводим заголовок второй страницы
    print(f'Заголовок второй страницы: {driver.title}')

    # Возвращаемся назад на первую страницу
    driver.back()

    # Проверяем с помощью assert, что мы действительно вернулись на первую страницу
    assert 'VK' in driver.title, f"Ошибка: ожидаемое значение 'VK', фактическое '{driver.title}'"

    # Обновляем страницу
    driver.refresh()

    # Получаем и выводим URL текущей страницы
    current_url = driver.current_url
    print(f"Текущий URL: {current_url}")

    # Переходим вперед на вторую страницу
    driver.forward()

    # Проверяем изменение URL
    new_current_url = driver.current_url
    if new_current_url != current_url:
        print("URL успешно сменился!")
    else:
        raise Exception("Ошибка: URL не поменялся.")
finally:
    # Завершаем работу драйвера
    driver.quit()