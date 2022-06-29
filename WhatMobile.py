from webbrowser import Chrome
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from IPython.display import display
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests


website='https://www.whatmobile.com.pk/'
path='/home/taha/Downloads/chromedriver_linux64 (1)/chromedriver'
driver=webdriver.Chrome(path)
driver.get(website)

search="OPPO"
list_of_image=list()

InputBox = driver.find_element_by_xpath("//input[@id='searchInput']")
InputBox.send_keys(search)
time.sleep(5)
try:
    InputBox.send_keys(Keys.RETURN)
    time.sleep(5)
except:
    pass
list_of_det=list()
list_of_links=list()
fulldet=driver.find_elements_by_xpath("//td[@class='BiggerText']")
# print(fulldet)

# list_of_det.append(fulldet.text)
# print(list_of_det)

for i in fulldet:
    det=i.find_element_by_xpath("//a[@class='BiggerText']")
    list_of_det.append(i.text)
# print(list_of_det)

    
for lnk in fulldet:
    lnks=lnk.find_element_by_tag_name("img")
    p=lnks.get_attribute('src')
    list_of_links.append(p)
# print(list_of_links)


# print(len(list_of_det))
# print(len(list_of_links))


d={'Mobile Title': list_of_det, 'Link': list_of_links}
df = pd.DataFrame(data=d)

display(df)

driver.close()