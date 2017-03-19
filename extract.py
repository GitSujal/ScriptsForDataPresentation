#extract data

import matplotlib.pyplot as plt
import fileinput
# Initialize buffers
X_buf = []
Y_buf = []
xa =[]
# Input file name with data being stored
print("Enter file Name with format")
filename = input()
print(filename)

#handling file input
with open (filename,'r') as jaf:
	for line in jaf:
		data = jaf.readline()
		if data!=[]: 
			james = data.split()
			y=james[6]
			Y_buf.append(float(y)
			xa =james[3].split(',')
			x =xa[0]
			X_buf.append(float(x))

#printing for debug			
# print("X_buf= ", X_buf)
# print("\n","Y_buf", Y_buf)

#ploting X and Y
plt.plot(Y_buf,X_buf)
plt.show()
