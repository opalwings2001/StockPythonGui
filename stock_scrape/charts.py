import os.path
import sqlite3
from turtle import fillcolor
from webbrowser import get
from matplotlib.pyplot import title, xlabel
from numpy import char
import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from stock_api_csv_parser import get_stock_csv_file
import plotly.express as px



#symbol = input("Stock Symbol: ").upper()
# file_name = get_stock_csv_file(symbol)
# print(f'Symbol: {symbol}')


def make_stock_chart(symbol, chart_type, output_size):
    
    stock_file = get_stock_csv_file(symbol,output_size)
    # file_name = f'{symbol}_DATA_DF.csv'

    # BASE_DIR = os.path.dirname(os.path.abspath('stockinfo_db.db'))
    # db_path = os.path.join(BASE_DIR, "stockinfo_db.db")
    # print(db_path)
    
    # conn = sqlite3.connect(db_path)
    # c = conn.cursor()
    # query = f'SELECT * from {file_name}'
    # df_stocks = pd.read_sql_query(query, conn)
    # conn.commit()

    # print(df_stocks.head())
    df_stocks = pd.read_csv(stock_file)

    fig_title = f'{symbol} {chart_type} CHART'

    layout_fig = go.Layout(xaxis=dict(title='Data') , title=fig_title)

    if(chart_type == 'CANDLESTICK'):

        fig_data = go.Candlestick(x = df_stocks['timestamp'], 
                    open= df_stocks['open'],
                    high= df_stocks['high'],
                    low=df_stocks['low'],
                    close=df_stocks['close'],
                    increasing_line_color='darkorchid',
                    decreasing_line_color='cornflowerblue')
        
        fig = go.Figure(data = fig_data, layout = layout_fig)

    elif(chart_type == 'TIME SERIES'):

        fig_data = go.Scatter(x=df_stocks['timestamp'], y=df_stocks['close'])

        fig = go.Figure(data = fig_data, layout = layout_fig)

    else:
        return "Invalid Chart Type..."
    

    stock_html_file = fig.write_html('chart_stock.html')
    plotly.offline.plot(fig, filename='chart_stock.html', config={'displayModeBar': True})

    if not os.path.exists("pdfs"):
        os.mkdir("pdfs")

    fig.write_image(f"pdfs/{fig_title}.pdf")
    # conn.close()
    return stock_html_file


# make_stock_chart('aapl', 'candlestick')

