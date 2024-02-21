from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

servObj = Service()
opts = Options()

name = "Mudasir"

driver = webdriver.Chrome(service=servObj, options=opts)
opts.add_experimental_option("detach",True)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alertTxt = alert.text
print(alertTxt)
alert.accept()
assert name in alertTxt
# alert.dismiss()
