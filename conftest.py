"""
Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py,
 который должен лежать в директории верхнего уровня в вашем проекте с тестами.
  Можно создавать дополнительные файлы conftest.py в других директориях,
   но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.
"""


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

"""
это добавит возможность писать опцию:
pytest -s -v --browser_name=firefox --reruns 1 --language=ru lesson6_step8_reruns.py
иначе будет ошибка:
pytest: error: unrecognized arguments: --language=ru
"""

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': browser_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", browser_language)

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()