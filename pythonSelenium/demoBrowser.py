from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
# for chrome
driver = webdriver.Chrome(service=service_obj)
# for firefox
# driver = webdriver.Firefox(service=service_obj)
# for Edge
# driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.forward()
driver.refresh()
driver.minimize_window()
driver.close()
