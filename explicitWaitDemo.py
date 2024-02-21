import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service()
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(4)

items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(items)
assert count > 0
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
for item in items:
    actualList.append(item.find_element(By.XPATH, "h4").text)
    item.find_element(By.XPATH, "div/button").click()
assert actualList == expectedList

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert sum == totalAmount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discAmount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert discAmount < sum
