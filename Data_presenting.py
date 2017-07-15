import matplotlib.pyplot as plt
import fileinput
#import matplotlib.animation as animation
import numpy as np



To_be_replaced = ["playerTransformPositions: x = ", " z = "]

filename = input("Type the file name also file format if anyother file format except .csv\n")
X_buf = []
Y_buf = []
X_sparse_buf = []
Y_sparse_buf = []
minthreshold = 0.00005;
#Formating file name
if '.' in filename:
	fullfilename  = filename
else :
	fullfilename = filename +'.csv' 

print("opening file  ", fullfilename);

#Handling File 
with open(fullfilename, 'r') as openfile:
	if openfile!=[]:
		print(fullfilename ," opened Successful")
		for line in openfile:
			line = line.replace(To_be_replaced[0],'')
			line = line.replace(To_be_replaced[1],'')
			#print(line)
			data = line.split(',')
			X_buf.append(float(data[0]))
			Y_buf.append(float(data[1]))
			
	else:
			print("Error opening file")
openfile.close()
print("File closed")
datalength = len(X_buf);
sparse_Factor  = 25;
# rang = ;

for i in range(0, int(datalength/sparse_Factor)):
	X_sparse_buf.append(X_buf[sparse_Factor*i]);
	Y_sparse_buf.append(Y_buf[sparse_Factor*i]);


#initialization
X_initial = X_buf[0];
Y_initial = Y_buf[0];
slope = [];
secondSlope = [];
# X_increment = X_initial;
# Y_initial = Y_initial;

# xdiff = [X_buf[n]-X_buf[n-1] for n in range(1,len(X_buf))];
#ydiff = [Y_buf[n]-Y_buf[n-1] for n in range(1,len(Y_buf))];
#slope = [(X_buf[n]-X_buf[n-1])/(Y_buf[n]-Y_buf[n-1]) for n in range(1,len(X_buf))];
#print(slope);

xdiff = np.diff(X_sparse_buf);
# np.all(xdiff[0] == xdiff);
# xDoubleDiff = np.diff(xdiff);
ydiff = np.diff(Y_sparse_buf);
# yDoubleDiff = np.diff(ydiff);

# print("X = ",xdiff);
# print(" Y = ",ydiff);

initial_slope = 0.0;
j = 0;
for i in range(0,len(X_sparse_buf)-2):
	if abs(xdiff[i+1]) > minthreshold:
		if abs(xdiff[i+1] - xdiff[i])  > minthreshold:
			 	fslope = ydiff[i+1]/xdiff[i+1];
		 		slope_diff = fslope - initial_slope;
		 		initial_slope = fslope;
		 		finalSlope = slope_diff/(xdiff[i+1] - xdiff[i]);
		 		secondSlope.append(finalSlope);
		 		print("slope ", finalSlope);
		else:
			print("X change null");
			j+=1;
# plt.plot(yDoubleDiff,xDoubleDiff);
# plt.show();
# print("Total data = ",len(X_buf));
# mean = np.average(slope);
# print("\n mean = ",mean);
print("\nTotal Data  = ", datalength);
print("\n Total Sparse data = ", len(X_sparse_buf));
plt.plot(Y_sparse_buf,X_sparse_buf,'r-');
plt.plot(Y_buf,X_buf);
plt.show();

axis = range(0,len(secondSlope));
print("\nTotal slopes calculated = ",len(secondSlope));
print("\n Total slopes skipped = ",j);
print("\n Total slope = ", len(secondSlope) + j);
print("\n Maximum value = ",np.amax(secondSlope));
print("\n Minimum Value = ",np.amin(secondSlope));

for i in range(0, len(secondSlope)):
	print("\nx = ", X_sparse_buf[i]," Y = ", Y_sparse_buf[i], "secondSlope = ", secondSlope[i]);
plt.plot(axis,secondSlope);
plt.scatter(axis,secondSlope);
plt.show();

# plt.plot(ydiff,xdiff,'r-');
# plt.title('test');
# plt.show();
# plt.plot(Y_buf,X_buf);
# plt.title('player movement');
# plt.show();

# #animation
# fig, ax = plt.subplots()
# line, = ax.plot(Y_buf,X_buf)

# def update(num, X_buf, Y_buf, line):
# 	line.set_data(X_buf[:num], Y_buf[:num])
# 	line.axes.axis([140, 270, 60, 230])
# 	return line,

# ani = animation.FuncAnimation(fig, update, len(X_buf), fargs=[X_buf, Y_buf, line], interval = 0.01, blit=True)
# plt.show()



