# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:24:47 2022

@author: Dipen
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from getpass import getpass
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



sheet_url = 'https://docs.google.com/spreadsheets/d/1TVI2-FRhkXuogFJOA3bfMRP7YD58QEhEJdCByM2Ao-0/edit#gid=943230711'
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

df = pd.read_csv(url_1)

df.columns = ['Product Name', 'Liquorkart-Catch', 'Boozbud-Catch',
       'Booze House- Catch', 'Hello Drink-Catch', 'Myliquoronline - Catch',
       'Mr Danks Liquor- Catch', 'PAULS LIQUOR STORE PTY. LTD. - Catch',
       'Liquor Geeks-Catch', 'Super Liquor Store-Catch',
       'The Gin Boutique-Catch', 'Secret Bottle Australia-Catch',
       'Cocktail Kit-Catch', 'Carlton United Breweries-Catch',
       'BulkPantry-Catch', 'Gold Emotion Australia-Catch',
       'Wine Relique-Catch', 'Booze&Barrels-Catch', 'Sippify-Catch',
       'GoodDrop-Catch', 'Drinks Network-Catch', 'Liqourkart-Kogan',
       'Boozbud -Kogan', 'Hello Drink -Kogan', 'Booze Barrels-Kogan',
       'Drinks Network-Kogan ', 'MyLiquoronline-Kogan',
       'The Drink Society- Kogan', 'Secret Bottle-Kogan',
       'Bickford’s Australia Pty Ltd- Kogan', 'Ozzies-Kogan','Sippify-kogan',
       'Liquorkart-Mydeal', 'Boozbud-Mydeal', 'Drinks Network-My Deal',
       'Hello Drink-Mydeal', 'Liquor Loot-Mydeal', 'Timex-Mydeal',
       'Mr Danks Liquor - My Deal', 'MyLiquoronline-Mydeal',
       'Secret Bottle-MyDeal', 'CocktailKit- Mydeal',
       'Carton United Breweries-Mydeal', 'Unnamed: 423', 'Booze Barrels-Mydeal',
       'Don Vassie Decanters-MyDeal', 'Unnamed: 46','Sippify-mydeal']

#%%
df7 = df[['Liquorkart-Catch', 'Boozbud-Catch',
       'Booze House- Catch', 'Hello Drink-Catch', 'Myliquoronline - Catch',
       'Mr Danks Liquor- Catch', 'PAULS LIQUOR STORE PTY. LTD. - Catch',
       'Liquor Geeks-Catch', 'Super Liquor Store-Catch',
       'The Gin Boutique-Catch', 'Secret Bottle Australia-Catch',
       'Cocktail Kit-Catch', 'Carlton United Breweries-Catch',
       'BulkPantry-Catch', 'Gold Emotion Australia-Catch',
       'Wine Relique-Catch', 'Booze&Barrels-Catch', 'Sippify-Catch',
       'GoodDrop-Catch', 'Drinks Network-Catch']]
df7.dropna(axis = 0, how = 'all',inplace=True)
#df7= df7[df7[['Boozbud-Catch','Booze_House-catch','hello_drink-catch','myliquoronline-catch','mr_Danks_Liquor_Catch']].str.match('https://www.catch.com.au/product/')]
options = Options()
Liquorkart_catch_url =[]
Boozbud_Catch_url =[]
Booze_House_catch_url = []
hello_drink_catch_url = []
myliquoronline_catch_url = []
mr_Danks_Liquor_Catch_url = []
PAULS_LIQUOR_STORE_PTY_LTD_Catch_url = []
Liquor_Geeks_Catch_url= []
Super_Liquor_Store_Catch_url=[]
The_Gin_Boutique_Catch_url=[]
Secret_Bottle_Australia_Catch_url=[]
Cocktail_Kit_Catch_url=[]
Carlton_United_Breweries_Catch_url=[]
BulkPantry_Catch_url = []
Gold_Emotion_Australia_Catch_url = []
Wine_Relique_Catch_url= []
Booze_Barrels_Catch_url=[]
Sippify_Catch_url=[]
GoodDrop_Catch_url=[]
Drinks_Network_Catch_url=[]

Liquorkart_catch_price =[]
Boozbud_Catch_price =[]
Booze_House_catch_price = []
hello_drink_catch_price = []
myliquoronline_catch_price = []
mr_Danks_Liquor_Catch_price = []
PAULS_LIQUOR_STORE_PTY_LTD_Catch_price = []
Liquor_Geeks_Catch_price= []
Super_Liquor_Store_Catch_price=[]
The_Gin_Boutique_Catch_price=[]
Secret_Bottle_Australia_Catch_price=[]
Cocktail_Kit_Catch_price=[]
Carlton_United_Breweries_Catch_price=[]
BulkPantry_Catch_price= []
Gold_Emotion_Australia_Catch_price = []
Wine_Relique_Catch_price= []
Booze_Barrels_Catch_price=[]
Sippify_Catch_price=[]
GoodDrop_Catch_price=[]
Drinks_Network_Catch_price=[]
#---------------------------------------------------
price=[]
Liquorkart_catch_url=[]
Liquorkart_catch_price=[]
df8=df7['Liquorkart-Catch'].dropna()
df8= df8[df8.str.match('https://www.catch.com.au/product/')]
for i in df8:
    print(i)
    i = ''.join(i)
    soup = BeautifulSoup(requests.get(i).text,"html.parser")
    Liquorkart_catch_url.append(i)
    mydivs = soup.find_all("div", {"class": "price--price-parts"})
    if mydivs == []:
        print(mydivs)
        Liquorkart_catch_price.append('0')
    else:
        print(mydivs[0].text) 
        Liquorkart_catch_price.append(mydivs[0].text)
            
   
res = pd.DataFrame()
res['Liquorkart_catch_url'] = Liquorkart_catch_url
#Boozbud_Catch_price = [ x for x in Boozbud_Catch_price if "Save$" not in x ]
res['Liquorkart_catch_price'] = Liquorkart_catch_price
df = df.join(res.set_index('Liquorkart_catch_url'), on='Liquorkart-Catch')      
df = df.drop_duplicates()
#---------------------------------------------------
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
price=[]
Boozbud_Catch_url=[]
Boozbud_Catch_price=[]
df8=df7['Boozbud-Catch'].dropna()
df8= df8[df8.str.match('https://www.catch.com.au/product/')]
for i in df8:
    print(i)
    i = ''.join(i)
    driver.get(i)
    Boozbud_Catch_url.append(i)
    try:      
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Boozbud_Catch_price.append('0')
            else:
                Boozbud_Catch_price.append(soup.text)
    except TimeoutException:
            Boozbud_Catch_price.append('0')
   
res = pd.DataFrame()
res['Boozbud_Catch_url'] = Boozbud_Catch_url
#Boozbud_Catch_price = [ x for x in Boozbud_Catch_price if "Save$" not in x ]
res['Boozbud_Catch_price'] = Boozbud_Catch_price
df = df.join(res.set_index('Boozbud_Catch_url'), on='Boozbud-Catch')      
df = df.drop_duplicates()
#-------------------------------------------------
price=[]
Booze_House_catch_url = []
Booze_House_catch_price = []
df9=df7['Booze House- Catch'].dropna()
df9= df9[df9.str.match('https://www.catch.com.au/product/')]
for i in df9:
    print(i)
    i = ''.join(i)
    Booze_House_catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Booze_House_catch_price.append('0')
            else:
                Booze_House_catch_price.append(soup.text)
    except TimeoutException:
            Booze_House_catch_price.append(0)
res = pd.DataFrame()
res['Booze_House_catch_url'] = Booze_House_catch_url
res['Booze_House_catch_price'] = Booze_House_catch_price
df = df.join(res.set_index('Booze_House_catch_url'), on='Booze House- Catch')      
df = df.drop_duplicates()
#------------------------------------------------------------
price=[]
df9=df7['Hello Drink-Catch'].dropna()
hello_drink_catch_url = []
hello_drink_catch_price = []
df9= df9[df9.str.match('https://www.catch.com.au/product/')]
for i in df9:
    print(i)
    i = ''.join(i)
    hello_drink_catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                hello_drink_catch_price.append('0')
            else:
                hello_drink_catch_price.append(soup.text)
    except TimeoutException:
        hello_drink_catch_price.append('0')
res = pd.DataFrame()
res['hello_drink_catch_url'] = hello_drink_catch_url
res['hello_drink_catch_price'] = hello_drink_catch_price
df = df.join(res.set_index('hello_drink_catch_url'), on='Hello Drink-Catch')      
df = df.drop_duplicates()

#---------------------------------------------------
price=[]
myliquoronline_catch_url=[]
myliquoronline_catch_price=[]
df10=df7['Myliquoronline - Catch'].dropna()
df10= df10[df10.str.match('https://www.catch.com.au/product/')]
for i in df10:
    print(i)
    i = ''.join(i)
    myliquoronline_catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                myliquoronline_catch_price.append('0')
            else:
                myliquoronline_catch_price.append(soup.text)
    except TimeoutException:
        myliquoronline_catch_price.append('0')
res = pd.DataFrame()
res['myliquoronline_catch_url'] = myliquoronline_catch_url
res['myliquoronline_catch_price'] = myliquoronline_catch_price
df = df.join(res.set_index('myliquoronline_catch_url'), on='Myliquoronline - Catch')      
df = df.drop_duplicates()

#--------------------------------------------------------
price=[]
mr_Danks_Liquor_Catch_url=[]
mr_Danks_Liquor_Catch_price = []
df11=df7['Mr Danks Liquor- Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    try:
        mr_Danks_Liquor_Catch_url.append(i)
        driver.get(i)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                mr_Danks_Liquor_Catch_price.append('0')
            else:
                mr_Danks_Liquor_Catch_price.append(soup.text)
    except TimeoutException:
        mr_Danks_Liquor_Catch_price.append('0')
   
res = pd.DataFrame()
res['mr_Danks_Liquor_Catch_url'] = mr_Danks_Liquor_Catch_url
res['mr_Danks_Liquor_Catch_price'] = mr_Danks_Liquor_Catch_price
df = df.join(res.set_index('mr_Danks_Liquor_Catch_url'), on='Mr Danks Liquor- Catch')      
df = df.drop_duplicates()

#----------------------------------------------------------------
price=[]
PAULS_LIQUOR_STORE_PTY_LTD_Catch_url=[]
PAULS_LIQUOR_STORE_PTY_LTD_Catch_price =[]
df11=df7['PAULS LIQUOR STORE PTY. LTD. - Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    PAULS_LIQUOR_STORE_PTY_LTD_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            if soup.text == '':
                PAULS_LIQUOR_STORE_PTY_LTD_Catch_price.append('0')
            else:
                PAULS_LIQUOR_STORE_PTY_LTD_Catch_price.append(soup.text)
                print(soup.text)
    except TimeoutException:
        PAULS_LIQUOR_STORE_PTY_LTD_Catch_price.append('0')
res = pd.DataFrame()
res['PAULS_LIQUOR_STORE_PTY_LTD_Catch_url'] = PAULS_LIQUOR_STORE_PTY_LTD_Catch_url
res['PAULS_LIQUOR_STORE_PTY_LTD_Catch_price'] = PAULS_LIQUOR_STORE_PTY_LTD_Catch_price
df = df.join(res.set_index('PAULS_LIQUOR_STORE_PTY_LTD_Catch_url'), on='PAULS LIQUOR STORE PTY. LTD. - Catch')      
df = df.drop_duplicates()

#------------------------------------------------------------------
price=[]
Liquor_Geeks_Catch_url =[]
Liquor_Geeks_Catch_price = []
df11=df7['Liquor Geeks-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Liquor_Geeks_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Liquor_Geeks_Catch_price.append('0')
            else:
                Liquor_Geeks_Catch_price.append(soup.text)
    except TimeoutException:
        Liquor_Geeks_Catch_price.append('0')
    
res = pd.DataFrame()
res['Liquor_Geeks_Catch_url'] = Liquor_Geeks_Catch_url
res['Liquor_Geeks_Catch_price'] = Liquor_Geeks_Catch_price
df = df.join(res.set_index('Liquor_Geeks_Catch_url'), on='Liquor Geeks-Catch')      
df = df.drop_duplicates()
#-------------------------------------------------------------------
price=[]
Super_Liquor_Store_Catch_url = []
Super_Liquor_Store_Catch_price = []
df11=df7['Super Liquor Store-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Super_Liquor_Store_Catch_url.append(i)
    try:
        driver.get(i)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Super_Liquor_Store_Catch_price.append('0')
            else:
                Super_Liquor_Store_Catch_price.append(soup.text)
    except TimeoutException:
        Super_Liquor_Store_Catch_price.append('0')
res = pd.DataFrame()
res['Super_Liquor_Store_Catch_url'] = Super_Liquor_Store_Catch_url
res['Super_Liquor_Store_Catch_price'] = Super_Liquor_Store_Catch_price
df = df.join(res.set_index('Super_Liquor_Store_Catch_url'), on='Super Liquor Store-Catch')      
df = df.drop_duplicates()
#-------------------------------------------------------------------------
price=[]
The_Gin_Boutique_Catch_url = []
The_Gin_Boutique_Catch_price = []
df11=df7['The Gin Boutique-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    The_Gin_Boutique_Catch_url.append(i)
    try:
        driver.get(i)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                The_Gin_Boutique_Catch_price.append('0')
            else:
                The_Gin_Boutique_Catch_price.append(soup.text)
    except TimeoutException:
        The_Gin_Boutique_Catch_price.append('0')
    
res = pd.DataFrame()
res['The_Gin_Boutique_Catch_url'] = The_Gin_Boutique_Catch_url
res['The_Gin_Boutique_Catch_price'] = The_Gin_Boutique_Catch_price
df = df.join(res.set_index('The_Gin_Boutique_Catch_url'), on='The Gin Boutique-Catch')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------------
price=[]
Secret_Bottle_Australia_Catch_url= []
Secret_Bottle_Australia_Catch_price = []
df11=df7['Secret Bottle Australia-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Secret_Bottle_Australia_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Secret_Bottle_Australia_Catch_price.append('0')
            else:
                Secret_Bottle_Australia_Catch_price.append(soup.text)
    except TimeoutException:
        Secret_Bottle_Australia_Catch_price.append('0')
        
res = pd.DataFrame()
res['Secret_Bottle_Australia_Catch_url'] = Secret_Bottle_Australia_Catch_url
res['Secret_Bottle_Australia_Catch_price'] = Secret_Bottle_Australia_Catch_price
df = df.join(res.set_index('Secret_Bottle_Australia_Catch_url'), on='Secret Bottle Australia-Catch')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------
price=[]
Cocktail_Kit_Catch_url= []
Cocktail_Kit_Catch_price = []
df11=df7['Cocktail Kit-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Cocktail_Kit_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Cocktail_Kit_Catch_price.append('0')
            else:
                Cocktail_Kit_Catch_price.append(soup.text)
    except TimeoutException:
        Cocktail_Kit_Catch_price.append('0')
    
res = pd.DataFrame()
res['Cocktail_Kit_Catch_url'] = Cocktail_Kit_Catch_url
res['Cocktail_Kit_Catch_price'] = Cocktail_Kit_Catch_price
df = df.join(res.set_index('Cocktail_Kit_Catch_url'), on='Cocktail Kit-Catch')      
df = df.drop_duplicates()
#-------------------------------------------------------------------------
price=[]
Carlton_United_Breweries_Catch_url =[]
Carlton_United_Breweries_Catch_price = []
df11=df7['Carlton United Breweries-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Carlton_United_Breweries_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Carlton_United_Breweries_Catch_price.append('0')
            else:
                Carlton_United_Breweries_Catch_price.append(soup.text)
    except TimeoutException:
        Carlton_United_Breweries_Catch_price.append('0')
res = pd.DataFrame()
res['Carlton_United_Breweries_Catch_url'] = Carlton_United_Breweries_Catch_url
res['Carlton_United_Breweries_Catch_price'] = Carlton_United_Breweries_Catch_price
df = df.join(res.set_index('Carlton_United_Breweries_Catch_url'), on='Carlton United Breweries-Catch')      
df = df.drop_duplicates()

#------------------------------------------------------------------------
price=[]
BulkPantry_Catch_url = []
BulkPantry_Catch_price = []
df11=df7['BulkPantry-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    BulkPantry_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                BulkPantry_Catch_price.append('0')
            else:
                BulkPantry_Catch_price.append(soup.text)
    except TimeoutException:
        BulkPantry_Catch_price.append('0')
res = pd.DataFrame()
res['BulkPantry_Catch_url'] = BulkPantry_Catch_url
res['BulkPantry_Catch_price'] = BulkPantry_Catch_price
df = df.join(res.set_index('BulkPantry_Catch_url'), on='BulkPantry-Catch')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------
# =============================================================================
# price=[]
# Gold_Emotion_Australia_Catch_url = []
# Gold_Emotion_Australia_Catch_price = []
# df11=df7['Gold Emotion Australia-Catch'].dropna()
# df11= df11[df11.str.match('https://www.catch.com.au/product/')]
# for i in df11:
#     print(i)
#     i = ''.join(i)
#     Gold_Emotion_Australia_Catch_url.append(i)
#     driver.get(i)
#     try:
#         WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
#         price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
#         if len(price) > 1:
#             price = [price[0]]
#         for i in price:
#             soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
#             print(soup.text)
#             if soup.text == '':
#                 Gold_Emotion_Australia_Catch_price.append('0')
#             else:
#                 Gold_Emotion_Australia_Catch_price.append(soup.text)
#     except TimeoutException:
#         Gold_Emotion_Australia_Catch_price.append('0')
# res = pd.DataFrame()
# res['Gold_Emotion_Australia_Catch_url'] = Gold_Emotion_Australia_Catch_url
# res['Gold_Emotion_Australia_Catch_price'] = Gold_Emotion_Australia_Catch_price
# df = df.join(res.set_index('Gold_Emotion_Australia_Catch_url'), on='Gold Emotion Australia-Catch')      
# df = df.drop_duplicates()
# 
# =============================================================================
#----------------------------------------------------------------------
price=[]
Wine_Relique_Catch_url = []
Wine_Relique_Catch_price = []
df11=df7['Wine Relique-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Wine_Relique_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Wine_Relique_Catch_price.append('0')
            else:
                Wine_Relique_Catch_price.append(soup.text)
    except TimeoutException:
       Wine_Relique_Catch_price.append('0')
res = pd.DataFrame()
res['Wine_Relique_Catch_url'] = Wine_Relique_Catch_url
res['Wine_Relique_Catch_price'] = Wine_Relique_Catch_price
df = df.join(res.set_index('Wine_Relique_Catch_url'), on='Wine Relique-Catch')      
df = df.drop_duplicates()
#---------------------------------------------------------------------------
price=[]
Booze_Barrels_Catch_url = []
Booze_Barrels_Catch_price = []
df11=df7['Booze&Barrels-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Booze_Barrels_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Booze_Barrels_Catch_price.append('0')
            else:
                Booze_Barrels_Catch_price.append(soup.text)
    except TimeoutException:
        Booze_Barrels_Catch_price.append('0')
res = pd.DataFrame()
res['Booze_Barrels_Catch_url'] = Booze_Barrels_Catch_url
res['Booze_Barrels_Catch_price'] = Booze_Barrels_Catch_price
df = df.join(res.set_index('Booze_Barrels_Catch_url'), on='Booze&Barrels-Catch')      
df = df.drop_duplicates()
#----------------------------------------------------------------------
price=[]
Sippify_Catch_url = []
Sippify_Catch_price = []
df11=df7['Sippify-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Sippify_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Sippify_Catch_price.append('0')
            else:
                Sippify_Catch_price.append(soup.text)
    except TimeoutException:
        Sippify_Catch_price.append('0')
res = pd.DataFrame()
res['Sippify_Catch_url'] = Sippify_Catch_url
res['Sippify_Catch_price'] = Sippify_Catch_price
df = df.join(res.set_index('Sippify_Catch_url'), on='Sippify-Catch')      
df = df.drop_duplicates()
#-------------------------------------------------------------------------
price=[]
GoodDrop_Catch_url = []
GoodDrop_Catch_price = []
df11=df7['GoodDrop-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    GoodDrop_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                GoodDrop_Catch_price.append('0')
            else:
                GoodDrop_Catch_price.append(soup.text)
    except TimeoutException:
        GoodDrop_Catch_price.append('0')
res = pd.DataFrame()
res['GoodDrop_Catch_url'] = GoodDrop_Catch_url
res['GoodDrop_Catch_price'] = GoodDrop_Catch_price
df = df.join(res.set_index('GoodDrop_Catch_url'), on='GoodDrop-Catch')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------
price=[]
Drinks_Network_Catch_url = []
Drinks_Network_Catch_price = []
df11=df7['Drinks Network-Catch'].dropna()
df11= df11[df11.str.match('https://www.catch.com.au/product/')]
for i in df11:
    print(i)
    i = ''.join(i)
    Drinks_Network_Catch_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div')))
        price=driver.find_elements_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        if len(price) > 1:
            price = [price[0]]
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Drinks_Network_Catch_price.append('0')
            else:
                Drinks_Network_Catch_price.append(soup.text)
    except TimeoutException:
        Drinks_Network_Catch_price.append('0')
res = pd.DataFrame()
res['Drinks_Network_Catch_url'] = Drinks_Network_Catch_url
res['Drinks_Network_Catch_price'] = Drinks_Network_Catch_price
df = df.join(res.set_index('Drinks_Network_Catch_url'), on='Drinks Network-Catch')      
df = df.drop_duplicates()
#%%
# =============================================================================
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
# 
# kogan = df[['Liqourkart-Kogan',
# 'Boozbud -Kogan', 'Hello Drink -Kogan', 'Booze Barrels-Kogan',
# 'Drinks Network-Kogan ', 'MyLiquoronline-Kogan',
# 'The Drink Society- Kogan', 'Secret Bottle-Kogan',
# 'Bickford’s Australia Pty Ltd- Kogan', 'Ozzies-Kogan', 'Sippify-kogan']]
# kogan.dropna(axis = 0, how = 'all',inplace=True)
# headers = {
#     'authority': 'www.kogan.com',
#     'accept': 'application/json',
#     'x-newrelic-id': 'XAABWFNAAAAFUlNWBw==',
#     'x-csrftoken': 'aj0PhkhjMI2T6wH0mIXYVe8TWdukgOz3ZnPoSNhDra0k4WHeJrCTVYefoRmoldJg',
#     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.kogan.com/',
#     'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': 'K.ID=92138085-d3e1-4161-9258-5e638ae0a59e; store_code=au; csrftoken=aj0PhkhjMI2T6wH0mIXYVe8TWdukgOz3ZnPoSNhDra0k4WHeJrCTVYefoRmoldJg; banner=banner; klc=53557222:Search%2CSearch; recently_viewed_au=53557222-46631031-46631037-60173052-64546871-77604727-46944782-47142592; datadome=.7SyUqc_VcPitCWwDDCF.hZQsqUVYXHCBS8hlk57YuOIrALTiTy6zmGiIS85.5vnDbJmLVna38mjj656HVAbB5jlesmjOSUllvyd7T3zK~0TuMd0qrWW_leHcGpraomx',
# }
# 
# 
# price=[]
# Liquorkart_kogan_url=[]
# Liquorkart_kogan_price=[]
# df8=kogan['Liqourkart-Kogan'].dropna()
# df8= df8[df8.str.match('https://www.kogan.com/au/buy/')]
# for i in df8:
#     print(i)
#     i = ''.join(i)
#     Liquorkart_kogan_url.append(i)
#     driver.get(i)
#     try:
#         WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="page-content"]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/h5/div/div[2]/span')))
#         price=driver.find_elements_by_xpath('//*[@id="page-content"]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/h5/div/div[2]/span')
#         if len(price) > 1:
#             price = [price[0]]
#         for i in price:
#             soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
#             print(soup.text)
#             if soup.text == '':
#                 Liquorkart_kogan_price.append('0')
#             else:
#                 Liquorkart_kogan_price.append(soup.text)
#     except TimeoutException:
#         Liquorkart_kogan_price.append('0')
#             
#    
# res = pd.DataFrame()
# res['Liquorkart_kogan_url'] = Liquorkart_kogan_url
# #Boozbud_Catch_price = [ x for x in Boozbud_Catch_price if "Save$" not in x ]
# res['Liquorkart_kogan_price'] = Liquorkart_kogan_price
# df = df.join(res.set_index('Liquorkart_catch_url'), on='Liquorkart-Catch')      
# df = df.drop_duplicates()
# 
# =============================================================================

#%%
df12 = df[['Liquorkart-Mydeal', 'Boozbud-Mydeal', 'Drinks Network-My Deal',
'Hello Drink-Mydeal', 'Liquor Loot-Mydeal', 'Timex-Mydeal',
'Mr Danks Liquor - My Deal', 'MyLiquoronline-Mydeal',
'Secret Bottle-MyDeal', 'CocktailKit- Mydeal',
'Carton United Breweries-Mydeal', 'Unnamed: 423', 'Booze Barrels-Mydeal',
'Don Vassie Decanters-MyDeal','Sippify-mydeal']]
df12.dropna(axis = 0, how = 'all',inplace=True)
#df9= df9[df9['mydeal'].str.match('https://www.mydeal.com.au/')]

options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
Liquorkart_Mydeal_url =[]
boozbud_mydeal_url = []
drinks_network_mydeal_url =[]
hello_drink_mydeal_url = []
liquor_loot_mydeal_url= []
Timex_Mydeal_url = []
Mr_Danks_Liquor_MyDeal_url = []
MyLiquoronline_Mydeal_url = []
Secret_Bottle_MyDeal_url=[]
CocktailKit_Mydeal_url=[]
Carton_United_Breweries_Mydeal_url = []
Booze_Barrels_Mydeal_url = []
Don_Vassie_Decanters_MyDeal_url=[]

Liquorkart_Mydeal_price =[]
boozbud_mydeal_price = []
drinks_network_mydeal_price =[]
hello_drink_mydeal_price = []
liquor_loot_mydeal_price= []
Timex_Mydeal_price = []
Mr_Danks_Liquor_MyDeal_price = []
MyLiquoronline_Mydeal_price = []
Secret_Bottle_MyDeal_price=[]
CocktailKit_Mydeal_price=[]
Carton_United_Breweries_Mydeal_price = []
Booze_Barrels_Mydeal_price = []
Don_Vassie_Decanters_MyDeal_price=[]

price = []
df13=df12['Liquorkart-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Liquorkart_Mydeal_url.append(i)
    driver.get(i)
    try :
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Liquorkart_Mydeal_price.append('0')
            else:
                Liquorkart_Mydeal_price.append(soup.text)
    except TimeoutException:
        Liquorkart_Mydeal_price.append('0')
            
res = pd.DataFrame()
res['Liquorkart_Mydeal_url'] = Liquorkart_Mydeal_url
res['Liquorkart_Mydeal_price'] = Liquorkart_Mydeal_price
df = df.join(res.set_index('Liquorkart_Mydeal_url'), on='Liquorkart-Mydeal')      
df = df.drop_duplicates()

#------------------------------------------------------------
price = []
df13=df12['Boozbud-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    boozbud_mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                boozbud_mydeal_price.append('0')
            else:
                boozbud_mydeal_price.append(soup.text)
    except TimeoutException:
        print(boozbud_mydeal_price.append('0'))
            
res = pd.DataFrame()
res['boozbud_mydeal_url'] = boozbud_mydeal_url
res['boozbud_mydeal_price'] = boozbud_mydeal_price
df = df.join(res.set_index('boozbud_mydeal_url'), on='Boozbud-Mydeal')      
df = df.drop_duplicates()

#-----------------------------------------------------------
price = []
drinks_network_mydeal_price =[]
drinks_network_mydeal_url=[]
df13=df12['Drinks Network-My Deal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                print(0)
                drinks_network_mydeal_url.append(i)
                drinks_network_mydeal_price.append(0)
            else:
                print(soup.text)
                drinks_network_mydeal_url.append(i)
                drinks_network_mydeal_price.append(soup.text)
    except TimeoutException:
        print(0,'this')
        boozbud_mydeal_price.append(0)
        
            
res = pd.DataFrame()
res['drinks_network_mydeal_url'] = drinks_network_mydeal_url
res['drinks_network_mydeal_price'] = drinks_network_mydeal_price
df = df.join(res.set_index('drinks_network_mydeal_url'), on='Drinks Network-My Deal')      
df = df.drop_duplicates()

#---------------------------------------------------------------
price = []
hello_drink_mydeal_url=[]
hello_drink_mydeal_price=[]
df13=df12['Hello Drink-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    hello_drink_mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                hello_drink_mydeal_price.append('0')
            else:
                hello_drink_mydeal_price.append(soup.text)
    except TimeoutException:
        hello_drink_mydeal_price.append('0')
            
res = pd.DataFrame()
res['hello_drink_mydeal_url'] = hello_drink_mydeal_url
res['hello_drink_mydeal_price'] = hello_drink_mydeal_price
df = df.join(res.set_index('hello_drink_mydeal_url'), on='Hello Drink-Mydeal')      
df = df.drop_duplicates()

#----------------------------------------------------------------
price = []
liquor_loot_mydeal_url=[]
liquor_loot_mydeal_price=[]
df13=df12['Liquor Loot-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    liquor_loot_mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                liquor_loot_mydeal_price.append('0')
            else:
                liquor_loot_mydeal_price.append(soup.text)
    except TimeoutException:
       liquor_loot_mydeal_price.append('0')
            
res = pd.DataFrame()
res['liquor_loot_mydeal_url'] = liquor_loot_mydeal_url
res['liquor_loot_mydeal_price'] = liquor_loot_mydeal_price
df = df.join(res.set_index('liquor_loot_mydeal_url'), on='Liquor Loot-Mydeal')      
df = df.drop_duplicates()
#----------------------------------------------------------
price = []
Timex_Mydeal_price=[]
Timex_Mydeal_url=[]
df13=df12['Timex-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Timex_Mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Timex_Mydeal_price.append('0')
            else:
                Timex_Mydeal_price.append(soup.text)
    except TimeoutException:
        Timex_Mydeal_price.append('0')
    
res = pd.DataFrame()
res['Timex_Mydeal_url'] = Timex_Mydeal_url
res['Timex_Mydeal_price'] = Timex_Mydeal_price
df = df.join(res.set_index('Timex_Mydeal_url'), on='Timex-Mydeal')      
df = df.drop_duplicates()
#------------------------------------------------------------
price = []
Mr_Danks_Liquor_MyDeal_url=[]
Mr_Danks_Liquor_MyDeal_price=[]
df13=df12['Mr Danks Liquor - My Deal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Mr_Danks_Liquor_MyDeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Mr_Danks_Liquor_MyDeal_price.append('0')
            else:
                Mr_Danks_Liquor_MyDeal_price.append(soup.text)
    except TimeoutException:
        Mr_Danks_Liquor_MyDeal_price.append('0')
    
            
res = pd.DataFrame()
res['Mr_Danks_Liquor_MyDeal_url'] = Mr_Danks_Liquor_MyDeal_url
res['Mr_Danks_Liquor_MyDeal_price'] = Mr_Danks_Liquor_MyDeal_price
df = df.join(res.set_index('Mr_Danks_Liquor_MyDeal_url'), on='Mr Danks Liquor - My Deal')      
df = df.drop_duplicates()
#--------------------------------------------------------------
# =============================================================================
# price = []
# MyLiquoronline_Mydeal_url=[]
# MyLiquoronline_Mydeal_price=[]
# df13=df12['MyLiquoronline-Mydeal'].dropna()
# df13= df13[df13.str.match('https://www.mydeal.com.au/')]
# for i in df9['MyLiquoronline-Mydeal'].dropna():
#     i = ''.join(i)
#     print(i)
#     MyLiquoronline_Mydeal_url.append(i)
#     driver.get(i)
#     try:
#         WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
#         price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
#         for i in price:
#             soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
#             print(soup.text)
#             if soup.text == '':
#                 MyLiquoronline_Mydeal_price.append('0')
#             else:
#                 MyLiquoronline_Mydeal_price.append(soup.text)
#     except TimeoutException:
#             MyLiquoronline_Mydeal_price.append('0')
# res = pd.DataFrame()
# res['MyLiquoronline_Mydeal_url'] = MyLiquoronline_Mydeal_url
# res['MyLiquoronline_Mydeal_price'] = MyLiquoronline_Mydeal_price
# df = df.join(res.set_index('MyLiquoronline_Mydeal_url'), on='MyLiquoronline-Mydeal')      
# df = df.drop_duplicates()
# =============================================================================
#-----------------------------------------------------------------
price = []
Secret_Bottle_MyDeal_url=[]
Secret_Bottle_MyDeal_price=[]
df13=df12['Secret Bottle-MyDeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Secret_Bottle_MyDeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Secret_Bottle_MyDeal_price.append('0')
            else:
                Secret_Bottle_MyDeal_price.append(soup.text)
    except TimeoutException:
       Secret_Bottle_MyDeal_price.append('0')
            
res = pd.DataFrame()
res['Secret_Bottle_MyDeal_url'] = Secret_Bottle_MyDeal_url
res['Secret_Bottle_MyDeal_price'] = Secret_Bottle_MyDeal_price
df = df.join(res.set_index('Secret_Bottle_MyDeal_url'), on='Secret Bottle-MyDeal')      
df = df.drop_duplicates()

#-----------------------------------------------------------------------
price = []
CocktailKit_Mydeal_price = []
CocktailKit_Mydeal_url =[]
df13=df12['CocktailKit- Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    CocktailKit_Mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                CocktailKit_Mydeal_price.append('0')
            else:
                CocktailKit_Mydeal_price.append(soup.text)
    except TimeoutException:
        CocktailKit_Mydeal_price.append('0')
            
res = pd.DataFrame()
res['CocktailKit_Mydeal_url'] = CocktailKit_Mydeal_url
res['CocktailKit_Mydeal_price'] = CocktailKit_Mydeal_price
df = df.join(res.set_index('CocktailKit_Mydeal_url'), on='CocktailKit- Mydeal')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------
price = []
Carton_United_Breweries_Mydeal_url = []
Carton_United_Breweries_Mydeal_price = [] 
df13=df12['Carton United Breweries-Mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Carton_United_Breweries_Mydeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Carton_United_Breweries_Mydeal_price.append('0')
            else:
                Carton_United_Breweries_Mydeal_price.append(soup.text)
    except TimeoutException:
        Carton_United_Breweries_Mydeal_price.append('0')
            
res = pd.DataFrame()
res['Carton_United_Breweries_Mydeal_url'] = Carton_United_Breweries_Mydeal_url
res['Carton_United_Breweries_Mydeal_price'] = Carton_United_Breweries_Mydeal_price
df = df.join(res.set_index('Carton_United_Breweries_Mydeal_url'), on='Carton United Breweries-Mydeal')      
df = df.drop_duplicates()
#-----------------------------------------------------------------------
# =============================================================================
# price = []
# Booze_Barrels_Mydeal_url = []
# Booze_Barrels_Mydeal_price = []
# df13=df12['Booze Barrels-Mydeal'].dropna()
# df13= df13[df13.str.match('https://www.mydeal.com.au/')]
# for i in df9['Booze Barrels-Mydeal'].dropna():
#     i = ''.join(i)
#     print(i)
#     Booze_Barrels_Mydeal_url.append(i)
#     driver.get(i)
#     try:
#         WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
#         price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
#         for i in price:
#             soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
#             print(soup.text)
#             if soup.text == '':
#                 Booze_Barrels_Mydeal_price.append('0')
#             else:
#                 Booze_Barrels_Mydeal_price.append(soup.text)
#     except TimeoutException:
#        Booze_Barrels_Mydeal_price.append('0')
# res = pd.DataFrame()
# res['Booze_Barrels_Mydeal_url'] = Booze_Barrels_Mydeal_url
# res['Booze_Barrels_Mydeal_price'] = Booze_Barrels_Mydeal_price
# df = df.join(res.set_index('Booze_Barrels_Mydeal_url'), on='Booze Barrels-Mydeal')      
# df = df.drop_duplicates()
# =============================================================================
#-----------------------------------------------------------------------
price = []
Don_Vassie_Decanters_MyDeal_url = []
Don_Vassie_Decanters_MyDeal_price = []
df13=df12['Don Vassie Decanters-MyDeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Don_Vassie_Decanters_MyDeal_url.append(i)
    driver.get(i)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Don_Vassie_Decanters_MyDeal_price.append('0')
            else:
                Don_Vassie_Decanters_MyDeal_price.append(soup.text)
    except TimeoutException:
        Don_Vassie_Decanters_MyDeal_price.append('0')
            
res = pd.DataFrame()
res['Don_Vassie_Decanters_MyDeal_url'] = Don_Vassie_Decanters_MyDeal_url
res['Don_Vassie_Decanters_MyDeal_price'] = Don_Vassie_Decanters_MyDeal_price
df = df.join(res.set_index('Don_Vassie_Decanters_MyDeal_url'), on='Don Vassie Decanters-MyDeal')      
df = df.drop_duplicates()
#--------------------------------------------------------------------------
price = []
Sippify_mydeal_url = []
Sippify_mydeal_price = []
df13=df12['Sippify-mydeal'].dropna()
df13= df13[df13.str.match('https://www.mydeal.com.au/')]
for i in df13:
    i = ''.join(i)
    print(i)
    Sippify_mydeal_url.append(i)
    driver.get(i)
    try: 
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')))
        price=driver.find_elements_by_xpath('//*[@id="product-attributes"]/tbody/tr[1]/td/hidden/span[2]')
        for i in price:
            soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
            print(soup.text)
            if soup.text == '':
                Sippify_mydeal_price.append('0')
            else:
                Sippify_mydeal_price.append(soup.text)
    except TimeoutException:
       Sippify_mydeal_price.append('0')
            
res = pd.DataFrame()
res['Sippify_mydeal_url'] = Sippify_mydeal_url
res['Sippify_mydeal_price'] = Sippify_mydeal_price
df = df.join(res.set_index('Sippify_mydeal_url'), on='Sippify-mydeal')      
df = df.drop_duplicates()
#%%
df =df[['Product Name','Liquorkart_catch_price', 'Boozbud_Catch_price',
'Booze_House_catch_price', 'hello_drink_catch_price',
'myliquoronline_catch_price', 'mr_Danks_Liquor_Catch_price',
'PAULS_LIQUOR_STORE_PTY_LTD_Catch_price', 'Liquor_Geeks_Catch_price',
'Super_Liquor_Store_Catch_price', 'The_Gin_Boutique_Catch_price',
'Secret_Bottle_Australia_Catch_price', 'Cocktail_Kit_Catch_price',
'Carlton_United_Breweries_Catch_price', 'BulkPantry_Catch_price', 'Wine_Relique_Catch_price',
'Booze_Barrels_Catch_price', 'Sippify_Catch_price',
'GoodDrop_Catch_price', 'Drinks_Network_Catch_price',
'Liquorkart_Mydeal_price', 'boozbud_mydeal_price',
'hello_drink_mydeal_price',
'liquor_loot_mydeal_price', 'Timex_Mydeal_price',
'Mr_Danks_Liquor_MyDeal_price',
'Secret_Bottle_MyDeal_price', 'CocktailKit_Mydeal_price',
'Carton_United_Breweries_Mydeal_price',
'Don_Vassie_Decanters_MyDeal_price', 'Sippify_mydeal_price']]

df.to_csv('C:\\Users\\dipen\\third_party_prices.csv')


