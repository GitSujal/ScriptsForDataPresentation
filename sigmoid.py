#Importing Necessary Models
import numpy as np
import pylab
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

filename = "Data_csvs/curvature_meanprobab1.csv" # Name of file with CSV data
csv = np.genfromtxt (filename, delimiter=",")
actual_gain = csv[:,0] #Extracting Actual Gain From csv file
less_probab1 = csv[:,1]*100 #Extracting Probability and converting it into percentage
less_probab2 = csv[:,2]*100
mean_probab = csv[:,3]*100


#Fitting Sigmoid Graph
def sigmoid(x, x0, b,a):
     y = 100/ (1 + a*np.exp(b*(x-x0)))
     return y

#Curve Fititng:

popt, pcov = curve_fit(sigmoid, actual_gain, mean_probab)


x = np.linspace(-0.2,0.2 ,5000)
y = sigmoid(x, *popt)
a = popt[2]
b = popt[1]
x0 = popt[0]

xvalue = x0-(np.log(a))/b;

print("The required equation is ",popt)
print("PSE = " ,xvalue)

#Plotting Error Bar
plt.errorbar(actual_gain,mean_probab, xerr=0, yerr=abs(less_probab1 - less_probab2),fmt='o',capsize=5,capthick=2,label="Errorbar")

#Plotting Actual Data and sigmoid fit graph
plt.plot(actual_gain,mean_probab,'o',label="Data",color="green")
plt.plot(x,y,label="Sigmoid Fit",color="Black")

#Plotting PSE refrence Lines
plt.plot([0,xvalue],[50,50],'r--',linewidth=1,alpha=0.4)
plt.plot([xvalue,xvalue],[0,50],'r--',linewidth=1,alpha=0.4)

#Printing PSE value and Sigmoid function parameters:
psetext = "PSE = " + str('%.3f'% xvalue)
if xvalue>=1:
  plt.annotate("",xy=(0.9, 5),xytext=(1, 5),arrowprops=dict(arrowstyle="<-",connectionstyle="arc3"),fontsize=7,)
  plt.annotate(psetext,xy=(xvalue, 5),xytext=((xvalue+0.1), 5),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=7,)
else:
  plt.annotate("",xy=(xvalue, 5),xytext=((xvalue-0.1), 5),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=7,)
  plt.annotate(psetext,xy=(1, 5),xytext=(1.1, 5),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=7,)


bbox_props = dict(boxstyle="square,pad=0.3")
t = plt.text(1.6,70, "a= ,b= ,x0=", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

text = "a="+str('%.3f'% a)+" b=" +str('%.3f'% b)+" X0= "+str('%.3f'% x0)
ann = plt.annotate(text,
                  xy=(1.75, 7), xycoords='data',
                  xytext=(1.6, 70), textcoords='data',
                  size=10, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  fc="w"), 
                  )

#Plotting Legends
plt.legend(loc='upper right',scatterpoints=1,numpoints=1,ncol=2,fontsize=8)

#Plotting X label, Y label and Title of Graph
plt.ylabel('Probability of < responses')
plt.xlabel('Value of applied Gain')
plt.grid(color='b', linestyle='--',linewidth=1,alpha=0.25)
plt.title("Regression fitting of Curvature gain responses II")

#Show the plot
plt.show()
