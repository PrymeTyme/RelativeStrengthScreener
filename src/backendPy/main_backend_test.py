from fetch_actual_ticker_names import stock_tickers_final,sector_stock_list
from fetch_api_data import fetch_tickers
from datetime import datetime as dt
from raw_data_to_json import save_sectors_to_json,save_stock_dict_to_json


import algo_data_to_json
import datetime


if __name__ == '__main__':

#1st  get actual ticker names from spdrwebsite , then save as backend
    #if error get ticker list from backup
    stock_tickers =  stock_tickers_final # wait till finished

#2nd fetch from tiingo api
#  if  error , skip and use from json

    start_date = dt.today() - datetime.timedelta(days=365)
    end_date = str(dt.today().strftime('%Y-%m-%d'))

    sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY']

    sectors_data = fetch_tickers(sectors,start_date,end_date) # raw ticker data  # wait till finished

    xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df = (fetch_tickers(x,start_date,end_date) for x in stock_tickers)  # wait

    ticker_data_list = [xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df] # raw ticker data # wait till finished
 
# 
# 3rd save raw ticker data (for charts) in json data
    stock_dict = dict(zip(sector_stock_list,ticker_data_list)) #wait

    save_stock_dict_to_json(stock_dict) # wait
    save_sectors_to_json(sectors_data) # wait

    algo_data_to_json
# 4th run rsc algo on sectors
#     save algo data to sector json

# 
# 5th run rsc algo on stocks
#     save algo data to stock json    


   # print('from fetch tickers name ' + str(stock_tickers_final))
    #print('from fethc api sectors ' + str(sectors_data)) ## need to dump to json aswell ?
   # print('from tech api stocks list ' + str(ticker_data_list))
