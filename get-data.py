import requests
import pandas as pd


url = 'https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'})
read_html_pandas_data = pd.read_html(r.text)
dataframe = read_html_pandas_data[0][:-1]