from fetch_actual_ticker_names import stock_tickers_final
from fetch_api_data import sectors_df, ticker_dataframe_list
from relative_strength_algo import rsc_algo_test
import pandas as pd

if __name__ == '__main__':
    print('from fetch tickers name ' + str(stock_tickers_final))
    print('from fethc api sectors ' + str(sectors_df)) ## need to dump to json aswell ?
    print('from tech api stocks list ' + str(ticker_dataframe_list))

    daily = slice(0, 2)
    weekly = slice(0, 6)
    monthly = slice(0, 31)
    yearly = slice(0, 366)


# run the rsc algo on sectors

    sector_daily = rsc_algo_test(sectors_df, daily)
    sector_weekly = rsc_algo_test(sectors_df, weekly)
    sector_monthly = rsc_algo_test(sectors_df, monthly)
    sector_yearly = rsc_algo_test(sectors_df, yearly)


# algo ouput into dataframe

    sector_daily_df = pd.DataFrame(sector_daily, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
    sector_weekly_df = pd.DataFrame(sector_weekly, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
    sector_monthly_df = pd.DataFrame(sector_monthly, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])
    sector_yearly_df = pd.DataFrame(sector_yearly, columns=['Ticker', 'RSC', 'Price', 'Percent Change', 'Index'])

    sector_daily_df.to_json(r'C:\Users\Sergej\hello-world\data\sector_daily_df_test.json')
    sector_weekly_df.to_json(r'C:\Users\Sergej\hello-world\data\sector_weekly_df_test.json')
    sector_monthly_df.to_json(r'C:\Users\Sergej\hello-world\data\sector_monthly_df_test.json')
    sector_yearly_df.to_json(r'C:\Users\Sergej\hello-world\data\sector_yearly_df_test.json')


# add stock tickers final backup file handling here ?

sectors_df.to_json(r'C:\Users\Sergej\hello-world\data\sectors_test.json')
