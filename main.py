import pandas as pd
from sklearn.model_selection import train_test_split
import get-data

X = dataframe[["Open", 'yesterday close', '2 day ago close', '3 day ago close' ,'4 day ago close']]
x_train, x_test, y_train, y_test = train_test_split(X, dataframe[["Close*"]], test_size=0.20, shuffle=False)


# LinearRegression
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(x_train,y_train)

pred = lm.predict(x_test)
print(pred)

#mean absolute error
from sklearn import metrics
print("mae: " + metrics.mean_absolute_error(y_test, pred))
