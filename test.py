import time

from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
time.sleep(2)

input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
time.sleep(2)

input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
time.sleep(2)

input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
time.sleep(2)

button = browser.find_element_by_css_selector("button.btn")
button.click()