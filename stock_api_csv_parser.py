import os.path
import sqlite3
import pandas as pd
import requests


def get_stock_csv_file(symbol,output_size):
    
    symbol = symbol.upper()
    output_size = output_size.lower()

    api_key = 'FI8KQOBSEG39RVXM'
    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY'

    params = {'function': function,
                'symbol': symbol,
                'datatype': 'csv',
                'apikey': api_key,
                'outputsize': output_size}

    response = requests.get(base_url, params=params)

    #save csv to file
    with open('stock_data.csv', 'wb') as file:
        file.write(response.content)

    stock_df = pd.read_csv('stock_data.csv') #create pandas df
    file_name = f'{symbol}_DATA_DF.csv'

    #put data frame in mySQL server
    BASE_DIR = os.path.dirname(os.path.abspath('stockinfo_db.db'))
    db_path = os.path.join(BASE_DIR, "stockinfo_db.db")
    print(db_path)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    #push pandas data fram in server
    stock_df.to_sql(file_name, conn, index=False, if_exists='replace')
    conn.commit()

    #save dataframe to csv
    stock_df.to_csv(file_name)

    print("CSV File Generated...")
    conn.close()
    return file_name

# symbol = 'spy'
# output_size = 'Compact'
# get_stock_csv_file(symbol, output_size)







