import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os
import pandas as pd
import base64
import csv


#CHANGE CSV NAME
df = pd.read_csv("hassani.csv",encoding= 'unicode_escape')
data_dict = df.to_dict('records')
barcodes = [item['Barcode'] for item in data_dict]
chrome_options = webdriver.ChromeOptions()



for barcode in barcodes:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/search?q=5285000201168&sca_esv=560946880&tbm=isch&sxsrf=AB5stBi24FB3-HvM3lZXc7ICrUqeHo3rAQ%3A1693299850492&source=hp&biw=1920&bih=995&ei=irTtZIeVG-PHkdUP96OoiAM&iflsig=AD69kcEAAAAAZO3CmjYgqhpcqRhnPykrz3kO7zPj6_kn&ved=0ahUKEwiHgtbAwYGBAxXjY6QEHfcRCjEQ4dUDCAc&uact=5&oq=5285000201168&gs_lp=EgNpbWciDTUyODUwMDAyMDExNjgyBBAjGCdIwQdQ3wRY3wRwAXgAkAEAmAHBAaABwQGqAQMwLjG4AQPIAQD4AQL4AQGKAgtnd3Mtd2l6LWltZ6gCCsICBxAjGOoCGCc&sclient=img")

    search_feild = driver.find_element(By.ID,'REsRA')
    search_feild.clear()
    time.sleep(1)
    search_feild.send_keys(barcode)
    search_feild.send_keys(Keys.ENTER)

    div_element = driver.find_element(By.CLASS_NAME,"bRMDJf.islir")


    img_element = div_element.find_element(By.TAG_NAME,"img")


    data_url = img_element.get_attribute("src")

    data_parts = data_url.split(",")
    image_data = data_parts[1]


    decoded_image_data = base64.b64decode(image_data)

    # CREATE A NEW FOLDER
    save_path = f"/Users/venkatesh/Desktop/hassani/{barcode}.jpg"  # Replace with your desired path and filename

    # Save the image
    with open(save_path, "wb") as image_file:
        image_file.write(decoded_image_data)

    print("Image downloaded and saved successfully.")
    driver.quit()

