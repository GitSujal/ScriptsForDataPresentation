import matplotlib.pyplot as plt
import fileinput
import matplotlib.animation as animation

To_be_replaced = ["playerTransformPositions: x = ", " z = "]

filename = input("Type the file name also file format if anyother file format except .txt")
X_buf = []
Y_buf = []



#Formating file name
if '.' in filename:
	fullfilename  = filename
else :
	fullfilename = filename +'.txt' 

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


#print(Y_buf,X_buf)
plt.plot(Y_buf,X_buf,'r-')
plt.title('test')
plt.show()


