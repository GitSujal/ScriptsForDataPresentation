import numpy as np
import matplotlib.pyplot as plt

filename = "final_data.csv"
csv = np.genfromtxt (filename, delimiter=",")
experience = csv[:,1]
Gain = csv[:,2]
 #Taking only experience and Actual Gain under consideration
#print(training_data)
target_Felt1 = csv[:,3] #Extracting target classes
target_Felt2 = csv[:,4]
colors = ["r", "g", "b"]
# less_exp = []
# more_exp = less_exp
# less_gain = less_exp
# more_gain = less_exp
for i in range(0,len(experience)):
	if target_Felt1[i] == 1:
		LG = plt.plot([Gain[i]], [experience[i]],'rs',markersize=10, color="red",alpha=0.35)
	else:
		MG = plt.plot([Gain[i]], [experience[i]],'g^',markersize=9, color="green",alpha=0.35)
plt.plot([0.5,1.5],[5,0],'b--')
plt.plot([Gain[0]],[experience[0]],'rs',markersize= 10,color="red",alpha=0.35,label="Less Gain with alpha 0.35")
plt.plot([Gain[15]],[experience[15]],'g^',markersize= 9,color="green",alpha=0.35,label="More Gain with alpha 0.35")
plt.ylabel('User Experience with VR')
plt.xlabel('Value of applied Gain')
plt.title('Scatter distribution of user experiencing less or more gain')
plt.ylim(-1,6)
plt.xlim(0.4,1.6)
plt.annotate('Linear separation', xy=(1, 2.5), xytext=(0.8,3.5),arrowprops=dict(facecolor='black', shrink=0.05),)

plt.legend(loc='upper right',scatterpoints=1,numpoints=1,ncol=2,fontsize=8)
# print("Lenght of less_exp",len(less_exp));
# print(len(more_exp))
# print(len(less_gain))
# print(len(more_gain))





plt.show()