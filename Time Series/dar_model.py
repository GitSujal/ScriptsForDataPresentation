import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyflux as pf
#matplotlib inline

filename = "Arun_Valley_export.csv"
data = pd.read_csv(filename)
data['Date'] = pd.to_datetime(data['Date']) 
data['date_delta'] = (data['Date'] - data['Date'].min())  / np.timedelta64(1,'D')
print(len(data))
print(len(data['date_delta']))
data.index = data['date_delta']


# plt.figure(figsize=(15,5))
# plt.plot(data.index,data['LTP'])
# plt.show()

model = pf.DAR(data=data, ar=4, integ=0, target='LTP')
x = model.fit("MLE")
x.summary(transformed=False)
model.plot_fit(figsize=(15,10))
# #print(x_data)
model.plot_predict(h=50, past_values=100, figsize=(15,5))