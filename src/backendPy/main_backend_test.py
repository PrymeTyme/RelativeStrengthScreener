from fetch_actual_ticker_names import stock_tickers_final,sector_stock_list
from fetch_api_data import fetch_tickers
from datetime import datetime as dt
from raw_data_to_json import raw_sectors_to_json,raw_stock_dict_to_json
from algo_data_to_json import sorted_sector_to_json,sorted_stock_to_json


import datetime
#import asyncio


if __name__ == '__main__':

#1st  get actual ticker names from https://www.sectorspdr.com/ 
    stock_tickers =  stock_tickers_final #

#2nd fetch raw data from tiingo api (if failed x times use backup json raw data)* needs to be implement in the future aswell as async?
    start_date = dt.today() - datetime.timedelta(days=365)
    end_date = str(dt.today().strftime('%Y-%m-%d'))

    sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY']

    sectors_data = fetch_tickers(sectors,start_date,end_date) # raw ticker data  for sectors

    xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df = (fetch_tickers(x,start_date,end_date) for x in stock_tickers)  

    ticker_data_list = [xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df] # raw ticker data for stocks
 

# 3rd save raw ticker data (for charts) in json data folder
    stock_dict = dict(zip(sector_stock_list,ticker_data_list)) 

    raw_sectors_to_json(sectors_data) 
    raw_stock_dict_to_json(stock_dict) 

# 4th run rsc algo on sectors ansd stocks and save sorted data in json folder
    daily = slice(0,2)
    weekly = slice(0,6)
    monthly = slice(0,31)
    yearly = slice(0,366)

    timeframes = [daily,weekly,monthly,yearly]
    string_timeframes = ['daily','weekly','monthly','yearly']

    sorted_sector_to_json(timeframes,string_timeframes)
    sorted_stock_to_json(timeframes,string_timeframes)



 