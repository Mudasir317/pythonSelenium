from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

servObj = Service()
driver = webdriver.Firefox(service=servObj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
opndWds = driver.window_handles
driver.switch_to.window(opndWds[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(opndWds[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
driver.quit()
