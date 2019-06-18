import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value")
x_inpute = x.text
y = calc(x_inpute)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()
