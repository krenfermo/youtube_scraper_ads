from selenium import webdriver 
#import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyperclip 
import sys


def buscar_video(driver):    
    
    from datetime import datetime
    import json
    from pytube import YouTube
    try:
        user_data =driver.find_element_by_css_selector('button.ytp-ad-skip-button.ytp-button')
       
        # datetime object containing current date and time
        now = datetime.now()
        #print("si", now)
        video = driver.find_element_by_css_selector('div.html5-video-container')
        sleep(3)
        print("hay ADS", now)
        webdriver.ActionChains(driver).context_click(video).perform()
        sleep(1)
        copia = driver.find_element_by_xpath("//*[contains(text(), 'Copiar informaci')]")
        
        sleep(1)
        copia.click()
        copia=pyperclip.paste()
        ini_string = json.loads(copia) 
        link = "https://www.youtube.com/watch?v=" +ini_string["addocid"]
        print(" URL DEL ADS:  https://www.youtube.com/watch?v=" +ini_string["addocid"])
 
        video = YouTube(link)
        video.streams.first().download()
        print("VIDEO DESCARGADO")
        #  ytp-play-button ytp-button
        return 1
    except:


        return 0
try:
    driver = webdriver.Chrome() 
    driver.get("https://www.youtube.com/watch?v=OidC4SkmHQI&list=RDMMOidC4SkmHQI")
except:
    print("Error driver, instala Google CHROME")

while True:
    busca = buscar_video(driver)
    if busca == 1:
        driver.quit()
        sys.exit()
    sleep(3)
