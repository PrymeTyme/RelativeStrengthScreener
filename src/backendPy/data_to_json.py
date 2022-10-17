from fetch_api_data import sectors_data, ticker_data_list
from fetch_actual_ticker_names import sector_stock_list

#sector_stock_list = ['xle','xlu','xlk','xlb','xlp','xly','xli','xlc','xlv','xlf','xlre']

stock_dict = dict(zip(sector_stock_list,ticker_data_list))

def save_stock_dict_to_json(stock_dict):
    for k,v in stock_dict.items():
        v.to_json('C:\\Users\\Sergej\\hello-world\\data\\stocks\\'+str(k)+'.json') # change to format

def save_sectors_to_json(sectors):
    sectors.to_json('C:\\Users\\Sergej\\hello-world\\data\\sectors\\sectors.json')
      
# sectors_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\sectors.json')
# xle_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xle_df.json')
# xlk_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xlx_df.json')
save_stock_dict_to_json(stock_dict)
save_sectors_to_json(sectors_data)
