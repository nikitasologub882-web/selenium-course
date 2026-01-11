# Импорт стандартного модуля time
# Используется для принудительных пауз (sleep)
# В реальных автотестах применять нежелательно, только для обучения/демо
import time

# Импорт основного класса WebDriver для управления браузером
from selenium import webdriver

# Менеджер драйвера — автоматически скачивает нужную версию ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Service используется для передачи пути к драйверу браузера
from selenium.webdriver.chrome.service import Service

# WebDriverWait — механизм явных ожиданий
# Позволяет ждать наступления нужного состояния элемента
from selenium.webdriver.support.ui import WebDriverWait

# Expected Conditions — набор готовых условий ожидания
from selenium.webdriver.support import expected_conditions as EC


# Создаём сервис ChromeDriver с автоматически установленным драйвером
service = Service(executable_path=ChromeDriverManager().install())

# Запускаем браузер Google Chrome
driver = webdriver.Chrome(service=service)

# Создаём объект явного ожидания
# 15 секунд — максимальное время ожидания
# poll_frequency=1 — проверка условия каждую секунду
wait = WebDriverWait(driver, 30, poll_frequency=1)


# Открываем тестовую страницу с динамическими элементами
driver.get("https://the-internet.herokuapp.com/dynamic_controls")


# Локатор кнопки Enable
# Кнопка включает (делает активным) поле ввода
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")

# Локатор текстового поля input
# Изначально поле заблокировано (disabled)
TEXT_FIELD = ("xpath", "//input[@type='text']")


# Ожидаем, пока кнопка Enable станет кликабельной,
# затем кликаем по ней
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()

# Принудительная пауза 3 секунды
# Нужна только для наглядности (увидеть изменение на странице)
time.sleep(3)


# Ожидаем, пока текстовое поле станет кликабельным
# (то есть перестанет быть disabled),
# затем вводим текст "Hello"
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")

# Пауза для визуального подтверждения введённого текста
time.sleep(3)


# Ожидаем, пока в атрибуте value текстового поля
# появится значение "Hello"
# Это корректная проверка для input-элементов
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))

# Пауза для визуального подтверждения успешной проверки
time.sleep(3)


# Если код дошёл до этой строки без ошибок,
# значит все шаги выполнены успешно
print("Все ок")
