import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyflux as pf
from datetime import datetime
#matplotlib inline

filename = "Arun_Valley_export.csv"
#csv = np.genfromtxt (filename, delimiter=",")
data = pd.read_csv(filename)
data['Date'] = pd.to_datetime(data['Date']) 
#print(data['Date'])   
data['date_delta'] = (data['Date'] - data['Date'].min())  / np.timedelta64(1,'D')

data.index = data['date_delta']
print(len(data))
print(len(data['date_delta']))
print(data.index)

data.loc[(data['date_delta']>=139), 'Book_Closure'] = 1;
data.loc[(data['date_delta']<157), 'Book_Closure'] = 0;
data.loc[(data['date_delta']>=256), 'Book_Closure'] = 1;
data.loc[(data['date_delta']<272), 'Book_Closure'] = 0;
data.loc[(data['date_delta']>=282), 'Listing'] = 1;
data.loc[(data['date_delta']<282), 'Listing'] = 0;
data.loc[(data['date_delta']>=287), 'New_Senior_Managment'] = 1;
data.loc[(data['date_delta']<287), 'New_Senior_Managment'] = 0;

data.loc[(data['date_delta']>=465), 'FPO'] = 1;
data.loc[(data['date_delta']<465), 'FPO'] = 0;


#Show Data
# plt.figure(figsize=(15,5))
# plt.plot(data.index,data['LTP'])
# plt.show()

# For ARIMAX model
model = pf.ARIMAX(data=data, formula='LTP~1+Book_Closure+Listing+New_Senior_Managment+FPO', ar=4, ma=4, family=pf.Normal())
x = model.fit("MLE")
x.summary()
model.plot_fit(figsize=(15,10))
model.plot_predict_is(h=50, figsize=(15,5))
# model.plot_predict(h=10, oos_data=data.iloc[-12:], past_values=100, figsize=(15,5))


