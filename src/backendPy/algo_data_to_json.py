import pandas as pd
import json
import os
import glob
from relative_strength_algo import rsc_algo


daily = slice(0,2)
weekly = slice(0,6)
monthly = slice(0,31)
yearly = slice(0,366)

timeframes = [daily,weekly,monthly,yearly]
string_timeframes = ['daily','weekly','monthly','yearly']

sector_counter = -1   #horrible way of doing it but it works... ;) (refactor later... XD)
stock_counter = -1 

with open(r'C:\Users\Sergej\hello-world\data\sectors\sectors.json') as f:
    sector_data = json.load(f)
    sector_data = pd.DataFrame.from_dict(sector_data)


for timeframe in timeframes:
    sector_name ="sector"
    sector_sorted = rsc_algo(sector_data,timeframe)
    sector_df = pd.DataFrame(sector_sorted, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
    sector_counter +=1 
    timeframe=string_timeframes[sector_counter]
    sector_df.to_json(fr'C:\Users\Sergej\hello-world\data\sectorSorted\{timeframe}\{sector_name}_{timeframe}.json')


# Stock Tickers rsc algo > to dataframe > to json

for filepath in glob.glob(os.path.join(r'C:\Users\Sergej\hello-world\data\stocks','*.json')):
    with open(filepath) as f:
        stock_data = json.load(f)
        stock_data = pd.DataFrame.from_dict(stock_data)

        for timeframe in timeframes:
            stock_sorted = rsc_algo(stock_data,timeframe)# if i use sector data it works with spy aswell ?
            stock_df = pd.DataFrame(stock_sorted, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
            index_name = stock_df.loc[0,'Index']
            index_name = index_name.lower()
            stock_counter += 1
            timeframe = string_timeframes[stock_counter]
            stock_df.to_json(fr'C:\Users\Sergej\hello-world\data\stockSorted\{timeframe}\{index_name}_{timeframe}.json')

            #print(timeframe +': \n'+str(stock_df)+'\n Index_Name = '+ index_name)

            if stock_counter >= 3 :   #horrible hard coded  but works ;) .. refactor later XD haha !
                stock_counter = -1


#pd.set_option('display.max_rows', None)
