import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

servObj = Service()
opts = Options()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=servObj,options=opts)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/#')
driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# IQ - when you update value dynamically through script, how do you extract the text?
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
driver.quit()
