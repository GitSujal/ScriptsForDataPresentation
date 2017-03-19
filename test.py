import numpy as np
import matplotlib.pyplot as plt
import fileinput
# evenly sampled time at 200ms intervals
# t = np.arange(0.0, 5.0, 0.2)
# x = np.random.rand(25)
# y = np.random.rand(25)
xfloat = []
yfloat = []
with open ("data.txt",'r') as jaf:
	for line in jaf:
		data = jaf.readline()
		james = data.strip().split(',')
		x = (float(james[0]) - 16.0)*20
		xfloat.append(x)
		y = (float(james[1]) - 16.0)*20
		yfloat.append(y)
print(xfloat)
print(yfloat)

plt.plot(yfloat,xfloat)
# plt.acorr(x, hold=None)
plt.show()	
