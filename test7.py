import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radioButton = browser.find_element_by_css_selector("[for = \"robotsRule\"]")
radioButton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
