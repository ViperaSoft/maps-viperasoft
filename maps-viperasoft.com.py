import os
import time

from selenium import webdriver


timeout = 10

sayac = 3

firma_sayisi = 0


op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
op.add_argument('--window-size=1920,1080')



driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

driver.get("https://www.google.com/maps")

time.sleep(4)

username = driver.find_element_by_xpath("//*[@id='searchboxinput']")

ara = "bağcılar dişçi"

username.send_keys(ara)

search_click = driver.find_element_by_id("searchbox-searchbutton")

search_click.click()

while True:

    try:

        # İLK FİRMA BEKLEYİŞ TIKLAMA

        # 3 5 7 9 şeklinde ilerliyor

      #  time.sleep(5)

        ilk_firma = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(sayac) + "]/div/a")

        ilk_firma.click()

       # ilk_firma.send_keys(Keys.END)
       # ilk_firma.send_keys(Keys.HOME)

        

       # WebDriverWait(driver, timeout).until(EC.presence_of_element_located(driver.find_element_by_xpath(
        #   '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(sayac) + "]/div/a').click()))

        #ilk_firma = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(sayac) + "]/div/a")))

        # KRİTİK NOKTA, BURAYI KAÇIRMA



        time.sleep(1.5)

        firma_sayisi+=1

        sayac+=2

      #  time.sleep(2)

    except:
        print("************ VERİLER BİTTİ PROGRAM SONRA ERDİ")
        break


    try:

        firma_isim = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/h1").text
        #firma_isim = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/h1"))).text
        print(firma_isim)


    except:

         firma_isim = "FİRMA YOK"
         print("FİRMA İSİM YOK")


    # KATEGORİ
