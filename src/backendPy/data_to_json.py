



def convert_json(dataframe):
    for i in dataframe:
        i.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\''+str(i)+'.json')  



#sectors_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\sectors.json') 
#xle_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xle_df.json')
#xlk_df.to_json(r'C:\Users\Sergej\hello-world\src\jsonData\xlx_df.json')