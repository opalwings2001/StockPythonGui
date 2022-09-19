import requests
import pandas as pd


def get_stock_symbol_list(keyword):

    api_key = 'FI8KQOBSEG39RVXM'
    base_url = 'https://www.alphavantage.co/query?'
    function = 'SYMBOL_SEARCH'
    keyword = keyword.upper()

    params = {'function': function,
                'keywords': keyword,
                'datatype': 'csv',
                'apikey': api_key}

    response = requests.get(base_url, params=params)

    with open('symbol_search.csv', 'wb') as file:
        file.write(response.content)

    syms_df = pd.read_csv('symbol_search.csv') #create pandas df
    symbol_list_df = syms_df[syms_df.columns[0]]
    symbol_list = list(symbol_list_df)

    return symbol_list

def creating_prefix(letter, alphabet, symb_list, prefix):

    for l in alphabet:
            key = f"{letter}{l}"
            print(key)
            prefix.append(key)
            if len(prefix) == 0:
                continue
            else:
                if len(symb_list) == 0:
                    symb_list = prefix
                else:
                    symb_list.append(prefix)


def every_ticker():

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symb_list = []
    prefix = []
    
    for letter in alphabet:
        prefix.append(letter)
        print(prefix)
        if len(prefix) == 0:
            continue
        else:
            if len(symb_list) == 0:
                symb_list = prefix
            else:
                symb_list.append(prefix)

        for lette in alphabet:
            for lett in alphabet:
                for let in alphabet:
                    for le in alphabet:
                        key = f"{letter}{lette}{lett}{let}{le}"
                        print(key)
                        prefix.append(key)
                        if len(prefix) == 0:
                            continue
                        else:
                            if len(symb_list) == 0:
                                symb_list = prefix
                            else:
                                symb_list.append(prefix)

            


    return symb_list


print(every_ticker())
