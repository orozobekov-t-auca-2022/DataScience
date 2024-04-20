import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter("ignore", category=FutureWarning)

df = pd.read_csv('BAC.csv')  # read the file
df = df[["Date", "Close"]]  # select only interesting part, such as Date and the price
# 'ds' stands for datestamp like '04.05.2024'
# 'y' stands for the target variable or the value you're trying to predict
df.columns = ["ds", "y"]

prophet = Prophet()
prophet.fit(df)  # pass in the historical dataframe

# let’s make predictions for the next 365 days
future = prophet.make_future_dataframe(periods=365)
forecast = prophet.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(200)

# let’s plot our predictions
prophet.plot(forecast, figsize=(20, 10))
plt.show()