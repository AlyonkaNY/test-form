import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
print(x)
input1 = browser.find_element(By.ID, 'answer')
y = (calc(x))
input1.send_keys(y)

browser.execute_script("window.scrollBy(0, 150);")

input2 = browser.find_element(By.ID, "robotCheckbox")
input2.click()
input3 = browser.find_element(By.ID, "robotsRule")
input3.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


'''button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()'''

time.sleep(10)

browser.quit()