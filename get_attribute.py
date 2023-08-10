from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/get_attribute.html
browser.get('http://suninjuly.github.io/get_attribute.html')

# Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()