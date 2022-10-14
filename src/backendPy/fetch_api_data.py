from tiingo import TiingoClient
from datetime import datetime as dt 
from fetch_actual_ticker_names import stock_tickers_final
import datetime
from dotenv import load_dotenv
import os

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


    
sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY']
#sectors_app_stocks = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE']

xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df = (get_tickers(x,start_date,end_date) for x in stock_tickers_final) ## get from fetchTickernames

ticker_data_list = [xle_df,xlu_df,xlk_df,xlb_df,xlp_df,xly_df,xli_df,xlc_df,xlv_df,xlf_df,xlre_df] # raw ticker data

sectors_data = get_tickers(sectors,start_date,end_date) # raw ticker data
