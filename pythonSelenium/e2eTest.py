from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service()
driver = webdriver.Chrome(service=servObj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[text()='Shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
driver.find_element(By.ID, "country").send_keys("India")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

successText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

assert "Success! Thank you! Your" in successText
