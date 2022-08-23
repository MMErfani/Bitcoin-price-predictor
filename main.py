import pandas as pd
from sklearn.model_selection import train_test_split


def get_data():
	import requests
	
	url = 'https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD'
	r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'})
	read_html_pandas_data = pd.read_html(r.text)
	dataframe = read_html_pandas_data[0][:-1]
	
	X = dataframe[["Open", 'yesterday close', '2 day ago close', '3 day ago close' ,'4 day ago close']]
	x_train, x_test, y_train, y_test = train_test_split(X, dataframe[["Close*"]], test_size=0.20, shuffle=False)


# LinearRegression
def linear_regression():
	from sklearn.linear_model import LinearRegression
	
	mymodel = LinearRegression()
	mymodel.fit(x_train,y_train)
	
	pred = mymodel.predict(x_test)
	
	
#mean absolute error
def mean_absolute_error():
	from sklearn import metrics
	print("mae: " + metrics.mean_absolute_error(y_test, pred))

def predictor():	
	thisClosePredict= mymodel.predict([[
    	dataframe["Open"][0],
    	dataframe["yesterday close"][0],
    	dataframe["2 days ago close"][0],
    	dataframe["3 days ago close"][0],
    	dataframe["4 days ago close"][0],]]
	)

	print(thisClosePredict)

def main():
	get_data()
	linear_regression()
	mean_absolute_error()
	predictor()
