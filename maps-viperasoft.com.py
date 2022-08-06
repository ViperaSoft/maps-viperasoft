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

time.sleep(10)

username = driver.find_element_by_xpath("//*[@id='searchboxinput']")

ara = "dişçi near istanbul"

username.send_keys(ara)

search_click.click()

time.sleep(10)

ilk_firma = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(sayac) + "]/div/a")

time.sleep(10)

firma_isim = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/h1").text

print(firma_isim)





