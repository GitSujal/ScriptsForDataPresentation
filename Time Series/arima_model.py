import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyflux as pf
#matplotlib inline

filename = "Arun_Valley_export.csv"
#csv = np.genfromtxt (filename, delimiter=",")
data = pd.read_csv(filename)
data['Date'] = pd.to_datetime(data['Date']) 
#print(data['Date'])   
data['date_delta'] = (data['Date'] - data['Date'].min())  / np.timedelta64(1,'D')
print(len(data))
print(len(data['Date']))

data.index = data['date_delta']

#Show Data
plt.figure(figsize=(15,5))
plt.plot(data.index,data['LTP'])
plt.show()

# # For Arima model
# model = pf.ARIMA(data=data, ar=4, ma=4, target='LTP', family=pf.Normal())
# x = model.fit("MLE")
# x.summary()
# model.plot_fit(figsize=(15,5))
# model.plot_predict_is(h=50, figsize=(15,5))
# model.plot_predict(h=20,past_values=20,figsize=(15,5))
#print(model.predict(h=10,intervals=False))

