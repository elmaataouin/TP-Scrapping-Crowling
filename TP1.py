import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

path = '/Users/elmaataouin/chromedriver/chromedriver.exe'
drive = webdriver.Chrome(path)

website = 'https://lematin.ma/express/2022/factures-energetique-alimentaire-seront-salees-maroc-entre-2022-2024/375134.html'
drive.get(website)


titreArticle = drive.find_element(By.ID, "title")
auteurArticle = drive.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/main/article/div[2]/div[1]/p/span[1]/a[2]")
contentArticle = drive.find_element(By.CLASS_NAME, "card-text")
dateArticle = drive.find_element(By.TAG_NAME, "time")


print('Titre :', titreArticle.text)
print('Auteur :', auteurArticle.text)
print('Content :', contentArticle.text)
print('Date :', dateArticle.text)
"""


website = 'file:///C:/Users/elmaataouin/Downloads/375134.html' #link local
drive.get(website)


titreArticle = drive.find_element(By.XPATH, '//*[@id="title"]')
auteurArticle = drive.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/main/article/div[2]/div[1]/p/span[1]/a[2]')
contentArticle = drive.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/main/article/div[3]/p[1]')
dateArticle = drive.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/main/article/div[2]/div[1]/p/time")


print('Titre :', titreArticle.text)
print('Auteur :', auteurArticle.text)
print('Content :', contentArticle.text)
print('Date :', dateArticle.text)
"""

time.sleep(2)
drive.quit()