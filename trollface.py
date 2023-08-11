import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/redirect_accept.html")
browser.find_element(By.CSS_SELECTOR, 'button').click()
browser.switch_to.window(browser.window_handles[1])



browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
print(x)
input1 = browser.find_element(By.ID, 'answer')
y = (calc(x))
input1.send_keys(y)


button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

time.sleep(10)

browser.quit()

