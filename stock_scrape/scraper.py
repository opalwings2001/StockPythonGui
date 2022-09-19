from http import server
from flask import Flask, render_template, request
from stock_api_csv_parser import get_stock_csv_file


# use flask to get html input and run
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('stocks.html')


@app.route('/stock-csv/',methods=['GET'])
def stock_csv():
    stock_symbol = request.form['myTicker'].upper()
    stock_file_name = get_stock_csv_file(stock_symbol)
    return stock_file_name

if __name__ == "__main__":
    app.run(debug=True)
