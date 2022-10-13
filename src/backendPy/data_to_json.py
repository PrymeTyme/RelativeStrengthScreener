from fetch_api_data import sectors_data, ticker_data_list

sector_stock_list = ['xle','xlu','xlk','xlb','xlp','xly','xli','xlc','xlv','xlf','xlre']

stock_dict = dict(zip(sector_stock_list,ticker_data_list))

print(stock_dict)


def convert_json(data_list):
    for k,v in data_list.items():
        v.to_json('C:\\Users\\Sergej\\hello-world\\data\\stocks\\'+str(k)+'.json')

# sectors_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\sectors.json')
# xle_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xle_df.json')
# xlk_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xlx_df.json')
convert_json(stock_dict)
