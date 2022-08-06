import os
import time
from selenium import webdriver
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
op.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
driver.get("https://www.google.com/maps")
input("BİR TUŞA BASINIZ"
