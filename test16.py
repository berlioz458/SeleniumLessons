import os 

from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name = browser.find_element_by_css_selector("input[name = \"firstname\"]")
name.send_keys("Kate")
lastname = browser.find_element_by_css_selector("input[name = \"lastname\"]")
lastname.send_keys("LastName")
email = browser.find_element_by_css_selector("input[name = \"email\"]")
email.send_keys("email@mail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

button1 = browser.find_element_by_id("file")
button1.send_keys(file_path)

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()
