'''
This program is written as an example interview program given from PRAMP.
This program counts the number of closed braces in any input string. 
A sting is said to have closed braces iff '(' is followed by ')' 
That means '(())' counts for two closed braces but '))((' doesn't count.
'''


def countclose(this):
	count = 0
	foundAt = 0
	index = 0
	if len(this) < 2: #Handeling Null and insufficient string length
		print("count = 0")
		return 0
	print("Length of string:",len(this))

	for i in range(0,len(this)):
		if this[i] == '(':
			if i <=foundAt:
				index = foundAt
			else:
				index = i
			ret_count,ret_foundAt = searchforlast(index=index,array=this,count=count)
			foundAt = ret_foundAt
			count = ret_count
		elif foundAt == -1:
				break
	return count
			

def searchforlast(index,array,count):
	if ')' in array[index:len(array)]:
		foundAt = array.index(')')
		array = array[:foundAt] + array[foundAt + 1:]
		count += 1
		print(foundAt)
		return count,foundAt
	else:
		return 0

inputstring = raw_input("Type the input sting:")
result = countclose(inputstring)
if result == -1:
	result = 0
print("The Number of closed braces =",result)
	


