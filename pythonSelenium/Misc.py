from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

cOpts = Options()
cOpts.add_argument("headless")
# cOpts.add_experimental_option("detach",True)
# cOpts.add_argument("--ignore-certificate-errors")

servObj = Service()
driver = webdriver.Chrome(service=servObj, options=cOpts)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("ss.png")
time.sleep(3)
