from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
btn = browser.find_element(By.ID, ("book"))
btn.click()
print("Booking Successful")

browser.execute_script("window.scrollBy(0, 150);")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
print(x)
input1 = browser.find_element(By.ID, 'answer')
y = (calc(x))
input1.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)

browser.quit()