from fetch_actual_ticker_names import stock_tickers_final
from fetch_api_data import sectors_df, ticker_dataframe_list

if __name__ == '__main__':
    print('from fetch tickers name '+ str(stock_tickers_final))
    print('from fethc api sectors '+ str(sectors_df))
    print('from tech api stocks list '+ str(ticker_dataframe_list))
    # add stock tickers final backup file handling here ?
