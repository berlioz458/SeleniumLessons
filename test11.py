import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text

z = int(x)+ int(y)
print(z)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(z))

button = browser.find_element_by_css_selector("button.btn")
button.click()