import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
op.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
driver.get("https://www.google.com/maps")

time.sleep(10)

# username = driver.find_element_by_xpath("//*[@id='searchboxinput']")


username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchboxinput']")))


ara = "dişçi near istanbul"

username.send_keys(ara)

# search_click = driver.find_element_by_id("searchbox-searchbutton")
search_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchbox-searchbutton")))



search_click.click()


time.sleep(10)

ilk_firma = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['3']/div/a")

ilk_firma.click()

time.sleep(10)

firma_isim = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/h1").text

print(firma_isim)
