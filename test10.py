from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

#первый вариант работы со списком: один раз нажали для раскрытия второй для выбора
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(1)").click()


#второй вариант работа, объявлен класс select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"