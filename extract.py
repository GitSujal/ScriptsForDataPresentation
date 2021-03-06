#extract data

import matplotlib.pyplot as plt
import numpy as np
import fileinput
import matplotlib.animation as animation
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


#animation
fig, ax = plt.subplots()
line, = ax.plot(Y_buf,X_buf)

def update(num, X_buf, Y_buf, line):
	line.set_data(X_buf[:num], Y_buf[:num])
	line.axes.axis([0, 250, 0, 250])
	return line,

ani = animation.FuncAnimation(fig, update, len(X_buf), fargs=[X_buf, Y_buf, line], interval = 25, blit=True)
plt.show()
