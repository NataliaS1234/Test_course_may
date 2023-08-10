from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

"""example"""
"""
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser.get(link)
    x1 = browser.find_element_by_css_selector('#input_value').text
    y = calc(x1)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    button.click()
    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(10)
    browser.quit()
"""