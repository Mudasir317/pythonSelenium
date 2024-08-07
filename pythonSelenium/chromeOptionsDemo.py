from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

servObj = Service()
cOpts = Options()
cOpts.add_argument("--set-maximized")
cOpts.add_argument("headless")
cOpts.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=servObj, options=cOpts)
