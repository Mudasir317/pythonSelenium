from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

service_obj = Service()
opts = Options()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=service_obj, options=opts)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
# XPATH - //tagname[@attr='value'] -> //input[@type='submit']
# CSS - tagname[attr='value'], #id .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("testing")
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
# static / single select dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("two-way")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

