import pandas as pd
import json

# get the sector into the list of stocks 
def flatten(input_list):
    output_list = []
    for element in input_list:
        if type(element) == list:
            output_list.extend(flatten(element))
        else:
            output_list.append(element)
    return output_list


#sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY']
sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE']



# update ticker holdings in sectors
sector_stock_list = ['xle','xlu','xlk','xlb','xlp','xly','xli','xlc','xlv','xlf','xlre']


try:
# fetch the actual ticker holdings in the sectors and clean the list of unwanted strings
    xle,xlu,xlk,xlb,xlp,xly,xli,xlc,xlv,xlf,xlre = (pd.read_csv('https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol='+str(x))
                                                            for x in sector_stock_list)

    sector_csv_list  = [xle,xlu,xlk,xlb,xlp,xly,xli,xlc,xlv,xlf,xlre] 

    xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers =(list(x.index.get_level_values(0)) 
                                                                                                                                       for x in sector_csv_list)

    ticker_list = [xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers]


    ticker_list_re = [xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers]

    xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers = [i[1:] 
                                                                                                                                        for i in ticker_list_re]


    stock_tickers = [xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers ]

    xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers = map(list,zip(
                                                                                                                        stock_tickers,sectors))

    stock_tickers_test = [xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers ]

    xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers = [flatten(x) for x in stock_tickers_test]

    stock_tickers = [xle_tickers,xlu_tickers,xlk_tickers,xlb_tickers,xlp_tickers,xly_tickers,xli_tickers,xlc_tickers,xlv_tickers,xlf_tickers,xlre_tickers ]

    stock_tickers_clean = [[x for x in y if str(x) != 'nan'] for y in stock_tickers]

    stock_tickers_final = [[x for x in y if x.isalpha()]for y in stock_tickers_clean]

    with open(r"C:\Users\Sergej\hello-world\data\tickerNamesBackup.json",'w') as f:
        json.dump(stock_tickers_final,f,indent=2)

except:
    print("catched error loading from backup")

    with open(r"C:\Users\Sergej\hello-world\data\tickerNamesBackup.json",'r') as f:
        stock_tickers_final =   json.load(f)
        


