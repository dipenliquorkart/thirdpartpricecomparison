# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 07:42:15 2022

@author: Dipen
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 06:06:42 2022

@author: Dipen
"""
import pandas as pd
import numpy as np 
from datetime import date
date = date.today()
d4 = date.strftime("%b-%d")

df = pd.read_csv('third_party_prices.csv',index_col=0)


lqprice = pd.read_csv('products.csv',index_col=0)

lqprice = lqprice[['Title','Cost per item','Variant Inventory Qty']]

df = df.join(lqprice.set_index('Title'), on='Product Name')     


df.columns = ['Product Name', 'Liquorkart_catch_price', 'Boozbud_Catch_price',
       'Booze_House_catch_price', 'hello_drink_catch_price',
       'myliquoronline_catch_price', 'mr_Danks_Liquor_Catch_price',
       'PAULS_LIQUOR_STORE_PTY_LTD_Catch_price', 'Liquor_Geeks_Catch_price',
       'Super_Liquor_Store_Catch_price', 'The_Gin_Boutique_Catch_price',
       'Secret_Bottle_Australia_Catch_price', 'Cocktail_Kit_Catch_price',
       'Carlton_United_Breweries_Catch_price', 'BulkPantry_Catch_price',
      'Wine_Relique_Catch_price',
       'Booze_Barrels_Catch_price', 'Sippify_Catch_price',
       'GoodDrop_Catch_price', 'Drinks_Network_Catch_price',
       'Liquorkart_Mydeal_price', 'boozbud_mydeal_price',
       'hello_drink_mydeal_price',
       'liquor_loot_mydeal_price', 'Timex_Mydeal_price',
       'Mr_Danks_Liquor_MyDeal_price',
       'Secret_Bottle_MyDeal_price', 'CocktailKit_Mydeal_price',
       'Carton_United_Breweries_Mydeal_price',
       'Don_Vassie_Decanters_MyDeal_price', 'Sippify_mydeal_price',
       'liquorkart_cost_price','Variant Inventory Qty']




#%%




df.to_csv(f"third_party_Price_comparison-{d4}.csv")
print('File Created')
        

