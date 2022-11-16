def get_ticker_names(metadata):
    v = {k:[dic[k] for dic in metadata] for k in metadata[0]}
    keys = v['ticker']
    values = v['name']

    ticker_names_dict = dict(zip(keys,values))

    return ticker_names_dict
