from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

servObj = Service()
opts = Options()
driver = webdriver.Chrome(service=servObj, options=opts)
opts.add_experimental_option("detach", True)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.CLASS_NAME, "blinkingText").click()

opndWds = driver.window_handles
driver.switch_to.window(opndWds[1])
paraStr = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
print(paraStr)
subStr = paraStr[19:49]
print(subStr)

driver.switch_to.window(opndWds[0])
driver.find_element(By.ID, "username").send_keys(subStr)
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "signInBtn").click()
errMsg = driver.find_element(By.XPATH, "//div[.='Incorrect username/password.']").text
print(errMsg)
