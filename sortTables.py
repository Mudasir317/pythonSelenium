import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

servObj = Service()
driver = webdriver.Chrome(service=servObj)
browSorVeg = []
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Top Deals']").click()
opndWds = driver.window_handles
driver.switch_to.window(opndWds[1])
time.sleep(3)
driver.find_element(By.XPATH, "//span[.='Veg/fruit name']").click()
vegWEs = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in vegWEs:
    browSorVeg.append(ele.text)

orgBrowSor = browSorVeg.copy()
browSorVeg.sort()

assert browSorVeg == orgBrowSor
