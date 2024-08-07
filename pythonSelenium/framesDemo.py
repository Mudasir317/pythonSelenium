from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

servObj = Service()
driver = webdriver.Chrome(service=servObj)

driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I'm able to automate frames")
driver.switch_to.default_content() # for switching to default window
assert driver.find_element(By.TAG_NAME, "h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor"
