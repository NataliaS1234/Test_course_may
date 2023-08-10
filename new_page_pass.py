from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_catch = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button_catch.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(3)
    # находим веб-элемент x
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

