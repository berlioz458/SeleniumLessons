import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id("treasure")
valuex = treasure.get_attribute("valuex")
y = calc(valuex)

input = browser.find_element_by_id("answer")
input.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
check.click()

radioButton = browser.find_element_by_id("robotsRule")
radioButton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
