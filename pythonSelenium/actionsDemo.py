from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

servObj = Service()
opts = Options()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=servObj, options=opts)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
# action.double_click()
# action.context_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
