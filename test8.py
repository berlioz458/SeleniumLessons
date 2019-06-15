from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


#Нашли радиокнопку по ключу
human_radio = browser.find_element_by_id("humanRule")

#По новому методу get_attribute получили true от checked
human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)

assert human_checked is not None

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robot radio: ", robots_checked)

assert robots_checked is None