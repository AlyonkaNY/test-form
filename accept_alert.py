import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# переключиться на окно с alert, а затем принять его с помощью команды accept()
'''alert = browser.switch_to.alert
alert.accept()'''
# получить текст из alert, используйте свойство text объекта alert
'''alert = browser.switch_to.alert
alert_text = alert.text'''

'''confirm.dismiss()'''
#  prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys()
'''prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()'''


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

confirm = browser.switch_to.alert
confirm.accept()


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