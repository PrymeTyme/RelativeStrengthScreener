from tiingo import TiingoClient
import pandas as pd
from datetime import datetime as dt 
import datetime
from dotenv import load_dotenv
import os
import numpy as np
from fetch_actual_ticker_names import stock_tickers_final,sector_stock_list

load_dotenv()

apiKey = os.getenv("API_KEY")
client = TiingoClient({'api_key':apiKey})
start_date = dt.today() - datetime.timedelta(days=365)
end_date = str(dt.today().strftime('%Y-%m-%d'))



def get_tickers(tickers,start_date,end_date):
     
    ticker_dataframe = client.get_dataframe(tickers,
                                      frequency ='daily',
                                      metric_name = 'adjClose', 
                                      startDate = start_date,
                                      endDate = end_date)
    
    ticker_dataframe = ticker_dataframe.iloc[::-1]
    
    return ticker_dataframe



def rsc_algo_test(dataframe,timeframe):
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


def fetch_metadata(tickers):
    ticker_metadata_list = []
    for ticker in tickers:
        ticker_metadata = client.get_ticker_metadata(ticker) 
        ticker_metadata_list.append(ticker_metadata) 

    return ticker_metadata_list

def fetch_metadata_stocks(tickers):
    ticker_metadata_list = []
    for list in tickers:
        for x in list:
            ticker_metadata = client.get_ticker_metadata(x) 
            ticker_metadata_list.append(ticker_metadata) 

    return ticker_metadata_list

def get_ticker_names(metadata):
    v = {k:[dic[k] for dic in metadata] for k in metadata[0]}
    keys = v['ticker']
    values = v['name']

    ticker_names_dict = dict(zip(keys,values))

    return ticker_names_dict


#sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY']


#sectors_df = get_tickers(sectors,start_date,end_date)

daily = slice(0,2)


#sector_daily = rsc_algo_test(sectors_df,daily)

#sector_daily_df =  pd.DataFrame(sector_daily,columns=['Ticker','RSC','Price','Percent Change','Index'])

#sector_metadata = fetch_metadata(sectors) 


#sector_names = get_ticker_names(sector_metadata)

#sector_daily_df['Name'] = sector_daily_df['Ticker'].map(sector_names)

test = [['XLK','CVS','GOOG'],['SPY','T','META'],['O','DISH','HAL']]

stocks = ['XLK','CVS','GOOG','SPY','T','META','O','DISH','HAL']

stocks_df = get_tickers(stocks,start_date,end_date)

stocks_daily = rsc_algo_test(stocks_df,daily)

stocks_daily_df =  pd.DataFrame(stocks_daily,columns=['Ticker','RSC','Price','Percent Change','Index'])

stocks_metadata = fetch_metadata_stocks(test)

stock_names = get_ticker_names(stocks_metadata)

stocks_daily_df['Name'] = stocks_daily_df['Ticker'].map(stock_names)

print(stock_names)

print(stocks_daily_df)

#print(sector_names)
#print(sector_names['XLF'])

#print(sectors_df)
#print(sector_daily)

#print(sector_daily_df)









pd.set_option('display.max_rows', None)
