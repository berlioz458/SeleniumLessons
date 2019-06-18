import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

btn = browser.find_element_by_id("book")

price = WebDriverWait(browser, 12).until(
EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
btn.click()

x = browser.find_element_by_id("input_value")
x_value = x.text
y = calc(x_value)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()