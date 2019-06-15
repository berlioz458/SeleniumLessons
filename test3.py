from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

#заполним данные о ФИО юзверя
#firstname = browser.find_element_by_name("firstname")
#firstname.send_keys("Kate");

#lastname = browser.find_element_by_name("lastname")
#lastname.send_keys("Shulinina");

#e-mail = browser.find_element_by_name("e-mail")
#e-mail.send_keys("test@mail.com");

elements = browser.find_elements_by_css_selector("input[type = text]")
for element in elements:
    element.send_keys("1")

button = browser.find_element_by_css_selector("button.btn")
button.click()

# не забывайте добавлять пустую строку в конце каждого файла в Python
