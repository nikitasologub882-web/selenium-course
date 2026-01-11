"""
АВТОМАТИЧЕСКИЙ ГЕНЕРАТОР И ВАЛИДАТОР ЛОКАТОРОВ ДЛЯ WEB-ЭЛЕМЕНТОВ

Основные задачи:
1. Автоматический поиск элементов по заданным HTML-тегам
2. Создание XPath локаторов на основе найденных элементов
3. Проверка валидности созданных локаторов
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def driver_init() -> WebDriver:
    """
    ИНИЦИАЛИЗАЦИЯ WEBDRIVER

    Создает и настраивает экземпляр Chrome WebDriver
    Возвращает: WebDriver - настроенный драйвер браузера
    """
    service = webdriver.ChromeService()  # Создаем сервис Chrome
    options = webdriver.ChromeOptions()  # Создаем объект опций браузера

    # Настройки окна браузера
    options.add_argument('--window-size=1920,1080')  # Устанавливаем размер окна 1920x1080

    # Опционально: headless режим (без графического интерфейса)
    # options.add_argument('--headless')  # Раскомментировать для запуска без окна браузера

    # Создаем и возвращаем драйвер с настройками
    return webdriver.Chrome(options=options, service=service)


def waiting(driver: WebDriver) -> WebDriverWait[WebDriver]:
    """
    СОЗДАНИЕ ОБЪЕКТА ОЖИДАНИЯ

    Параметры:
        driver: WebDriver - драйвер браузера
    Возвращает: WebDriverWait - объект для ожидания элементов
    """
    # Создаем объект ожидания с таймаутом 5 секунд
    # Используется для ожидания появления элементов на странице
    return WebDriverWait(driver=driver, timeout=5)


def collect_tags(driver: WebDriver,
                 wait: WebDriverWait[WebDriver],
                 url: str,
                 tags: tuple[str, ...]
                 ) -> dict[str, list[WebElement]]:
    """
    СБОР ВСЕХ ЭЛЕМЕНТОВ ПО УКАЗАННЫМ ТЕГАМ

    Параметры:
        driver: WebDriver - драйвер браузера
        wait: WebDriverWait - объект ожидания
        url: str - адрес страницы для анализа
        tags: tuple[str, ...] - кортеж тегов для поиска (например: ('div', 'a', 'p'))

    Возвращает: dict[str, list[WebElement]] - словарь, где ключи - теги, значения - списки элементов
    """
    elms = {}  # Пустой словарь для хранения найденных элементов

    # 1. ОТКРЫТИЕ СТРАНИЦЫ
    driver.get(url)  # Переходим по указанному URL

    # 2. ОЖИДАНИЕ ЗАГРУЗКИ СТРАНИЦЫ
    # Ждем появления любого элемента с классом "card-body"
    # Это индикатор того, что основное содержимое страницы загрузилось
    wait.until(ec.presence_of_element_located(('xpath', '//div[@class="card-body"]')))

    # 3. ПОИСК ЭЛЕМЕНТОВ ПО КАЖДОМУ ТЕГУ
    for item in tags:
        # Находим ВСЕ элементы с указанным тегом на странице
        # Используем XPath: //item - найдет все элементы с тегом 'item'
        elms[item] = driver.find_elements('xpath', f'//{item}')

    return elms


def create_locators(elms: dict[str, list[WebElement]]) -> dict[str, list[tuple[str, str]]]:
    """
    СОЗДАНИЕ XPATH ЛОКАТОРОВ ДЛЯ НАЙДЕННЫХ ЭЛЕМЕНТОВ

    Параметры:
        elms: dict[str, list[WebElement]] - словарь с найденными элементами

    Возвращает: dict[str, list[tuple[str, str]]] - словарь с созданными локаторами
        Формат: {'div': [('xpath', '//div[@id="header"]'), ...]}
    """
    locators: dict[str, list[tuple[str, str]]] = {}  # Словарь для хранения локаторов

    # Перебираем все найденные элементы
    for item in elms.items():
        tag, web_elms = item  # tag = 'div', 'a', 'p'; web_elms = список элементов

        for web_elem in web_elms:
            temp = None  # Временная переменная для хранения значения атрибута
            value = None  # Кортеж (значение_атрибута, тип_атрибута)

            # 1. ПРИОРИТЕТНЫЙ ПОИСК АТРИБУТА 'id'
            # Если у элемента есть id, используем его
            if temp := web_elem.get_attribute('id'):
                value = (temp, 'id')  # Формат: ('header', 'id')

            # 2. ЕСЛИ НЕТ 'id', ИЩЕМ 'class'
            elif temp := web_elem.get_attribute('class'):
                value = (temp, 'class')  # Формат: ('navbar', 'class')

            # 3. СОЗДАНИЕ XPATH ЛОКАТОРА
            if temp:  # Если нашли какой-либо атрибут (id или class)
                # Создаем XPath вида: //tag[@attribute="value"]
                xpath_expression = f'//{tag}[@{value[1]}="{value[0]}"]'

                # Добавляем локатор в словарь
                # setdefault создает пустой список, если ключа еще нет
                locators.setdefault(tag, []).append(('xpath', xpath_expression))

    return locators


def check_tags(driver: WebDriver,
               wait: WebDriverWait[WebDriver],
               locators: dict[str, list[tuple[str, str]]]
               ) -> None:
    """
    ПРОВЕРКА ВАЛИДНОСТИ СОЗДАННЫХ ЛОКАТОРОВ

    Параметры:
        driver: WebDriver - драйвер браузера
        wait: WebDriverWait - объект ожидания
        locators: dict[str, list[tuple[str, str]]] - словарь с локаторами для проверки
    """
    # 1. ОБНОВЛЕНИЕ СТРАНИЦЫ
    # Обновляем страницу, чтобы проверить, что локаторы работают после перезагрузки
    driver.refresh()

    # 2. ОЖИДАНИЕ ЗАГРУЗКИ СТРАНИЦЫ
    wait.until(ec.presence_of_element_located(('xpath', '//div[@class="card-body"]')))

    # 3. ПРОВЕРКА КАЖДОГО ЛОКАТОРА
    for tag in locators.keys():
        # enumerate добавляет индекс (начинается с 1)
        for index, locator in enumerate(locators[tag], 1):
            try:
                # *locator распаковывает кортеж ('xpath', '//div[@id="header"]')
                # в driver.find_element('xpath', '//div[@id="header"]')
                driver.find_element(*locator)

                # Вывод успешного результата
                # :<120 - форматирование вывода для выравнивания
                print(f'{index:<3}# {locator[-1]:<120} Found')

            except NoSuchElementException:
                # Вывод, если элемент не найден
                print(f'{index:<3}# {locator[-1]:<117} NotFound')


def main() -> None:
    """
    ГЛАВНАЯ ФУНКЦИЯ ПРОГРАММЫ
    Координирует весь процесс создания и проверки локаторов
    """
    # 1. НАСТРОЙКА ПАРАМЕТРОВ
    tags = ('div', 'a', 'p')  # HTML-теги для поиска
    url = 'https://hyperskill.org/tracks'  # URL страницы для анализа

    # 2. ИСПОЛЬЗОВАНИЕ КОНТЕКСТНОГО МЕНЕДЖЕРА
    # 'with' автоматически закроет драйвер после завершения блока
    with driver_init() as driver:
        # 3. ИНИЦИАЛИЗАЦИЯ ОЖИДАНИЯ
        wait = waiting(driver)

        # 4. СБОР ЭЛЕМЕНТОВ ПО ТЕГАМ
        elms = collect_tags(driver, wait, url, tags)

        # 5. СОЗДАНИЕ ЛОКАТОРОВ НА ОСНОВЕ НАЙДЕННЫХ ЭЛЕМЕНТОВ
        locators = create_locators(elms)

        # 6. ПРОВЕРКА ВАЛИДНОСТИ СОЗДАННЫХ ЛОКАТОРОВ
        check_tags(driver, wait, locators)


# ТОЧКА ВХОДА ПРОГРАММЫ
if __name__ == '__main__':
    """
    Этот блок выполняется ТОЛЬКО при прямом запуске файла,
    а не при импорте как модуля
    """
    main()