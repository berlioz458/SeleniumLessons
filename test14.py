import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id("input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x)
x_value = x.text
y = calc(x_value)

input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)

check = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()

radioButton = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
radioButton.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
