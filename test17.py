import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("alert('Hello!');")

alert = browser.switch_to.alert
alert_text = alert.text # получить текст из алерта
time.sleep(3)
alert.accept() # подтвердить алерт

browser.execute_script("confirm('Hello!');")
confirm = browser.switch_to.alert
time.sleep(3)
confirm.accept()
# confirm.dismiss()

browser.execute_script("prompt('Hello!');")
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
time.sleep(3)
prompt.accept()
