from fetch_actual_ticker_names import sector_stock_list

#sector_stock_list = ['xle','xlu','xlk','xlb','xlp','xly','xli','xlc','xlv','xlf','xlre']

#stock_dict = dict(zip(sector_stock_list,ticker_data_list))

def raw_stock_dict_to_json(stock_dict):
    for k,v in stock_dict.items():
        v.to_json('C:\\Users\\Sergej\\hello-world\\data\\stocks\\'+str(k)+'.json') # change to format

def raw_sectors_to_json(sectors):
    sectors.to_json('C:\\Users\\Sergej\\hello-world\\data\\sectors\\sectors.json')
      
