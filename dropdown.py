from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

a = browser.find_element(By.ID, "num1").text
b = browser.find_element(By.ID, "num2").text
x = str(int(a) + int(b))

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(x))

button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()

time.sleep(5)

browser.quit()
