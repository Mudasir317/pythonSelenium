import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

servObj = Service()
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(items)
assert count > 0
for item in items:
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
txt = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(txt)
assert "Code applied ..!" in txt
