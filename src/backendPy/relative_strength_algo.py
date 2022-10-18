import pandas as pd
#import json
#import os
#import glob
#from fetch_api_data import sectors_data, ticker_data_list


def rsc_algo(dataframe,timeframe): ## when using json files i meed to reverse the columns values order
    dataframe = dataframe.iloc[::-1]  ## when using json files i meed to reverse the columns values order
    columns = list(dataframe)
    base_instrument = dataframe.columns.values[-1]
    sorted_symbols=[]
    
    for column in columns:
        if column == base_instrument:
            continue
        sorted_symbols.append(tuple((column,(dataframe[column][timeframe] / dataframe[base_instrument][timeframe])[::-1].pct_change().sum(),dataframe[column][0],
                                     round((dataframe[column][timeframe][::-1].pct_change().sum())*100,2),base_instrument))) # output tuple with ticker,rsc
        
        sorted_symbols.sort( key=lambda x: x[1],reverse=True)
    return sorted_symbols


#daily = slice(0,2)
#weekly = slice(0,6)
#monthly = slice(0,31)
#yearly = slice(0,366)

#timeframes = [daily,weekly,monthly,yearly]
#string_timeframes = ['daily','weekly','monthly','yearly']

#with open(r'C:\Users\Sergej\hello-world\data\sectors\sectors.json') as f:
 #   sector_data = json.load(f)
  #  sector_data = pd.DataFrame.from_dict(sector_data)

#count = -1   #horrible way of doing it but it works... ;) (refactor later... XD)

#for i in timeframes:
 #   sector="sector"
  #  x = rsc_algo(sector_data,i)
   # y = pd.DataFrame(x, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
    #count +=1 
    #timeframe=string_timeframes[count]
    #y.to_json(fr'C:\Users\Sergej\hello-world\data\sectorSorted\{timeframe}\{sector}_{timeframe}.json')


# Stock Tickers rsc algo > to dataframe > to json

#for filepath in glob.glob(os.path.join(r'C:\Users\Sergej\hello-world\data\stocks','*.json')):
 #   with open(filepath) as f:
  #      data = json.load(f)
   #     data = pd.DataFrame.from_dict(data)

    #    for i in timeframes:
     #       x = rsc_algo(data,i)
      #      y = pd.DataFrame(x, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
       #     index = y.loc[0,'Index']
        #    count += 1
        #    timeframe=string_timeframes[count]
        #    y.to_json(fr'C:\Users\Sergej\hello-world\data\stockSorted\{timeframe}\{index}_{timeframe}.json')

            #print(timeframe +': '+str(y)+' Index = '+index)
         #   if count >= 3 :   #horrible hard coded  but works ;) .. refactor later XD haha !
          #      count = -1


pd.set_option('display.max_rows', None)
