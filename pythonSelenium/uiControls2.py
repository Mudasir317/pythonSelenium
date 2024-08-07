from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serObj = Service()
opts = Options()
driver = webdriver.Chrome(service=serObj, options=opts)
opts.add_experimental_option('detach', True)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

radiobts = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobts[1].click()
assert radiobts[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

