import csv
from ctypes.wintypes import tagMSG
import PySimpleGUI as sg
import plotly
import os.path
from charts import make_stock_chart
from stock_symbol_list import get_stock_symbol_list
from stock_api_csv_parser import get_stock_csv_file

sg.theme('GreenMono')
check1 = True
check2 = True

layout1 = [
    [sg.Text("Welcome to Stock-Scrape!")],
    [sg.Text("Your Stock Data Charting Service", auto_size_text=10)],
    [sg.Button("Next")]
]

window1 = sg.Window(
    "StockScrape",
    layout1,
    finalize=True,
    element_justification="center",
    font="Cambria",
)

while check1:
    event1, values1 = window1.read()
    if event1 is None or event1 == sg.WIN_CLOSED:
        check2 = False
        break
    if event1 == 'Next':
        print("Continue...")
        check1 = False

window1.close()
#get input from user for stock symbol and chart type
sym_vals = get_stock_symbol_list("a")
output_tip = "There are two options in terms of the number of data points that can be analyzed. \nThe full version will return 20 years worth of data points. \nThe compact version will return data from the last 100 days"
chart_tip = "A candlestick chart is good for representing price movement through a \ngiven day, since it includes the opening, daily high, daily low and closing price. \nA time series chart will show the movement of the closing price of a given stock over \ntime."
    

layout2 = [
        [sg.Text("Please read the following and then fill out the fields below.")],
        [sg.Text(chart_tip),],
        [sg.Text(output_tip),],
        
        [sg.HorizontalSeparator()],

        [
            sg.Text("Stock Symbol: "),
            # sg.Input(enable_events=True,key="-TICKER-", size=(41,10)),
            sg.Push(),
            sg.Combo(values=sym_vals,enable_events=True,bind_return_key=True,key="-TICKER-",size=(40,10)),  
            
        ],
        [
            sg.Text("Output of Data Points: "),
            sg.Push(),
            sg.Combo(values=['Full', 'Compact'],size = (40, 10), enable_events=True, bind_return_key=True,key="-OTYPE-"),
            # sg.Popup("There are two options in terms of the number of data points that can be analyzed. The full option will return 20 years worth of data points. The compact version will return data from the last 100 days",title="Amount of Data Options"),
            
        ],
        [
            # sg.ButtonMenu("Chart Type: ",menu_def=[['pf', 'cd', 'ts'],['Point and Figure', 'Candlestick', 'Time Series']], key = "-ctype-"),
            sg.Text("Chart Type: "),
            sg.Push(),
            sg.Combo(values=['Candlestick', 'Time Series'],size = (40, 10), enable_events=True, bind_return_key=True,key="-CTYPE-"),
            # sg.Popup("This service gives the option of generating a candlestick or time series chart. A candlestick chart is good as representing price movement through each given day, including the daily high and lows. A time series chart will show the movement of the closing price of a given stock.",title="Type of Charts"),
        ],

        [
            sg.Button("Submit"),
            sg.Button("Reset"),
        ],

        [sg.HorizontalSeparator()],


        [
            sg.Text("File Name...", auto_size_text=5, click_submits=True ,background_color='#BCDEE3', key="-FILE NAME-"),
        
        
            sg.Button(
                "Copy",
                key='-COPY FILE PATH-',
            ),
        ]
  
]

# create window

window2 = sg.Window(
    "StockScrape",
    layout2,
    finalize=True,
    icon=r"stocks_stock2.png",
    element_justification="left",
    auto_close_duration=60,
    font="Cambria",
)


#event2 loop

while check2:
    if check2 == False:
        break
    event2, values2 = window2.read()
    if event2 is None or event2 == sg.WIN_CLOSED:
        break
    
    window2['-TICKER-'].set_tooltip("Enter your stock or mutual fund token")
    output_tip = "There are two options in terms of the number of data points that can be analyzed. \nThe full version will return 20 years worth of data points. \nThe compact version will return data from the last 100 days"
    window2['-OTYPE-'].set_tooltip(output_tip)
    chart_tip = "A candlestick chart is good for representing price movement through a given day, since it includes the opening, daily high, daily low and closing price. \nA time series chart will show the movement of the closing price of a given stock over time."
    window2['-CTYPE-'].set_tooltip(chart_tip)
    
    if event2 == 'Submit':
        symbol = values2['-TICKER-']
        chart_type = values2['-CTYPE-']
        output_size = values2['-OTYPE-']

        print(f"You entered {symbol} and {chart_type}")
        symbol = symbol.upper()
        chart_type = chart_type.upper()
        output_size = output_size.lower()
        fig = make_stock_chart(symbol, chart_type, output_size)
        stock_csv = get_stock_csv_file(symbol,output_size)
        base_dir = os.path.dirname(os.path.abspath('pdfs'))
        pdf_path = os.path.join(base_dir, "pdfs")

        window2['-FILE NAME-'].update(pdf_path)
    if event2 == 'Copy':
        print("Copied!")
    elif event2 == 'Save As':
        print("Saving file...")
    if event2 == 'Reset':
        window2['-TICKER-'].update('')
        window2['-CTYPE-'].update('')
        window2['-OTYPE-'].update('')

window2.close()
