from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")


username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchboxinput']")))


ara = "dişçi near istanbul"

username.send_keys(ara)

# search_click = driver.find_element_by_id("searchbox-searchbutton")
search_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchbox-searchbutton")))

search_click.click()

ilk_firma = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['3']/div/a")

print(ilk_firma)
