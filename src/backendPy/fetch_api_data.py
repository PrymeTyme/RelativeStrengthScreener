from tiingo import TiingoClient
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("API_KEY")
client = TiingoClient({'api_key':apiKey})


def fetch_tickers(tickers,start_date,end_date):
     
    ticker_dataframe = client.get_dataframe(tickers,
                                      frequency ='daily',
                                      metric_name = 'adjClose', 
                                      startDate = start_date,
                                      endDate = end_date)
    
    ticker_dataframe = ticker_dataframe.iloc[::-1]
    
    return ticker_dataframe

def fetch_metadata(ticker):
    ticker_metadata = client.get_ticker_metadata(ticker)  

    return ticker_metadata  

