## Imports 
import os 
import webbrowser
import requests
import selenium
from selenium import webdriver
import re
import urllib.parse
from flask import Flask
import time
# import scrapy
# import watchdog
# import psutil
# import yara

driver = webdriver.Chrome()
driver.get('https://www.google.com')

last_scanned_url = ''

try :

    print('agent is currently scanning')
    while True : 

        current_site = driver.current_url

        if current_site != last_scanned_url :
            print (f"new site detected! {current_site}")
            
            print(f'agent is scanning{current_site}')
        if not current_site.startswith("https"):
            print(f"Site Unsafe! https not found! {current_site}")

        time.sleep(50)

except Exception as e:
    print(f"Agent stopped: {e}")
finally:
    driver.quit()





## site scanner /// Are they responding  ??? 

# req = requests.get('https://www.cnn.com/')
# if req.status_code == 200:
#     print (f'site succesfully scanned! : {req}')
# else :
#     print('fail')
# print(req)

# ## Interaction with webbrowser

# driver = webdriver.Chrome()
# driver.get('https://www.cnn.com')
# print(driver.title)


# webbrowser.open('https://www.google.com')