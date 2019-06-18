import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button1 = browser.find_element_by_css_selector("button.trollface")
button1.click()

new_window = browser.window_handles[1]
old_window = browser.window_handles[0]

browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value")
x_value = x.text
y = calc(x_value)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()