from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

path = r'COALINDIA.NS.csv'
coalDf=pd.read_csv(path,parse_dates=['Date'])

coalDf

# Leave jan 1 2023 data
monthlyTime = coalDf['Date'][:-1]
highPrice = coalDf['High'][:-1]

coalDf.describe()

coalDf.info()

import plotly.graph_objects as go
import numpy as np

def polynomial_fit(n):
    degree = n
    coefficients = np.polyfit(X, y, degree)
    poly_func = np.poly1d(coefficients)
    fit = poly_func(X)

    plt.scatter(X, y, label='Data points')
    plt.plot(X, fit, color='red', label='Polynomial fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Regression')
    plt.legend()
    plt.show()
    return poly_func

y = coalDf['Close'][:-1]
X = coalDf["Date"][:-1].values.astype('datetime64[M]').astype(int)

linear_model = polynomial_fit(1)
quadratic_model = polynomial_fit(2)
higher_model = polynomial_fit(4)
print(linear_model(coalDf["Date"].iloc[-1:].values.astype('datetime64[M]').astype(int))[0])
print(quadratic_model(coalDf["Date"].iloc[-1:].values.astype('datetime64[M]').astype(int))[0])
print(higher_model(coalDf["Date"].iloc[-1:].values.astype('datetime64[M]').astype(int))[0])

coalDf

def interpolate(coalDf):
  df = coalDf.copy()
  df['Date'] = pd.to_datetime(df['Date'])
  df = df.set_index('Date').resample('D')
  df = df.re
  df.interpolate(method='linear')
  fig = go.Figure(data=[go.Scatter(x = df['Date'], y = coalDf['High']),go.Scatter(x = df['Date'], y = df['High'])])
  fig.show()

# interpolate(coalDf)
df = coalDf.copy()
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date').resample('D')
# df = df.re
# df.interpolate(method='linear')
print(df)
# fig = go.Figure(data=[go.Scatter(x = df['Date'], y = coalDf['High']),go.Scatter(x = df['Date'], y = df['High'])])
# fig.show()

df

df = coalDf.copy()
df

"""## ARMA"""

df=pd.read_csv(path,parse_dates=['Date'])

df.describe()

df.head()

import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.tsa.arima_model import ARMA

df['High'].plot()

df_stationarityTest = adfuller(df['High'], autolag='AIC')

df_stationarityTest

print("P-value: ", df_stationarityTest[1])

pacf = plot_pacf(df['High'])

acf = plot_acf(df['High'])

train_data = df['High'][:len(df)-50]
test_data = df['High'][len(df)-50:]

import statsmodels.api as sm
model = sm.tsa.ARIMA(df['High'], order=(1,0,11))
# model = ARMA(train_data, order=(1,11))

model_fit = model.fit()

print(model_fit.summary())

predictions = model_fit.predict(start=df.index[0], end=df.index[-1])
residuals = test_data - predictions

plt.figure(figsize=(10,4))

plt.plot(df['High'])
plt.plot(predictions)

plt.legend(('Data', 'Predictions'), fontsize=16)

plt.title('First Difference of Coal stock', fontsize=20)
plt.ylabel('High price', fontsize=16)

print('Root Mean Squared Error:', np.sqrt(np.mean(residuals**2)))

def ad_test(dataset):
     dftest = adfuller(dataset, autolag = 'AIC')
     print("1. ADF : ",dftest[0])
     print("2. P-Value : ", dftest[1])
     print("3. Num Of Lags : ", dftest[2])
     print("4. Num Of Observations Used For ADF Regression:", dftest[3])
     print("5. Critical Values :")
     for key, val in dftest[4].items():
         print("\t",key, ": ", val)
ad_test(df['High'])

"""## ARIMA

"""

pip install pmdarima

from pmdarima import auto_arima
stepwise_fit = auto_arima(df['High'], trace=True,
suppress_warnings=True)

model=sm.tsa.ARIMA(df['High'],order=(1,1,13))
model=model.fit()
model.summary()

predictions = model.predict(start=df.index[0], end=df.index[-1])
residuals = test_data - predictions

plt.figure(figsize=(10,4))

plt.plot(df['High'])
plt.plot(predictions)

plt.legend(('Data', 'Predictions'), fontsize=16)

plt.title('First Difference of Coal stock', fontsize=20)
plt.ylabel('High price', fontsize=16)

print('Root Mean Squared Error:', np.sqrt(np.mean(residuals**2)))

result = adfuller(df['High'])

print("ADF Statistic:", result[0])
print("p-value:", result[1])

if result[1] > 0.05:
    differenced_data = df['High'].diff().dropna()
    result_diff = adfuller(differenced_data)

    print("ADF Statistic after differencing:", result_diff[0])
    print("p-value after differencing:", result_diff[1])

    if result_diff[1] <= 0.05:
        d = 1
    else:
        d = 2
else:
    d = 0

print("Chosen differencing order (d):", d)

"""## Moving avg"""

df1 = df.copy()
df1 = df1['High'].to_frame()

# calculating simple moving average
# using .rolling(window).mean() ,
# with window size = 1
df1['SM30'] = df1['High'].rolling(5).mean()

# removing all the NULL values using
# dropna() method
df.dropna(inplace=True)

# printing Dataframe

df1[['High', 'SM30']].plot(label='RELIANCE',
                                  figsize=(16, 8))

df1

df['High'][0]