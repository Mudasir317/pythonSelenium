from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

servObj = Service()
opts = Options()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=servObj, options=opts)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
