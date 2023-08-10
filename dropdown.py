
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    sum1 = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(sum1))

    button = browser.find_element_by_tag_name(".btn").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:

    time.sleep(10)

    browser.close()
    browser.quit()