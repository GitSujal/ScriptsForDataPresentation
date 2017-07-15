# Clear Data before manipulating

import fileinput
import numpy as np
import csv

To_be_replaced = ["playerTransformPositions: x = ", " z = "]

filename = input("Type the file name also file format if anyother file format except .txt\n")
X_buf = []
Y_buf = []
minthreshold = 0.00005;

#Formating file name
if '.' in filename:
	fullfilename  = filename
else :
	fullfilename = filename +'.txt' 

print("opening file  ", fullfilename);

newFileName = filename+".csv"
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
np.savetxt(newFileName,(X_buf),delimiter=',', newline='\n')
np.savetxt(newFileName,(Y_buf),delimiter=',', newline='\n')

# with open(newFileName, "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(a)



