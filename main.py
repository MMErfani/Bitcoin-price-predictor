import pandas as pd
from sklearn.model_selection import train_test_split

def get_data():
  import requests
      
  url = 'https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD'
  r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'})
  read_html_pandas_data = pd.read_html(r.text)
  dataframe = read_html_pandas_data[0][:-1]
      
      
  close = dataframe["Close*"]
  close_yest = close.shift(-1)
  close_2d = close.shift(-2)
  close_3d = close.shift(-3)
  close_4d = close.shift(-4)
      
      
  dataframe['yesterday close'] = close_yest
  dataframe['2 days ago close'] = close_2d
  dataframe['3 days ago close'] = close_3d
  dataframe['4 days ago close'] = close_4d
      
  dataframe.dropna(inplace=True)

  X = dataframe[["Open", 'yesterday close', '2 days ago close', '3 days ago close' ,'4 days ago close']]
  x_train, x_test, y_train, y_test = train_test_split(X, dataframe[["Close*"]], test_size=0.20, shuffle=False)

# LinearRegression
def linear_regression():
  from sklearn.linear_model import LinearRegression
      
  mm = LinearRegression()
  mm.fit(x_train,y_train)
      
  pred = mm.predict(x_test)

#mean absolute error
def mean_absolute_error():
  from sklearn import metrics
  print("mae: " + str(metrics.mean_absolute_error(y_test, pred)))

def predictor():    
    thisClosePredict = mm.predict([[
        dataframe["Open"][0],
        dataframe["yesterday close"][0],
        dataframe["2 days ago close"][0],
        dataframe["3 days ago close"][0],
        dataframe["4 days ago close"][0],]]
    )
    return str(thisClosePredict[0][0])


get_data()
linear_regression()
mean_absolute_error()
print(str(predictor()))
    
