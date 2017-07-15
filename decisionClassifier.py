# Script for Decision tree Classifier
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import pydotplus 

#For reading the data in CSV format
filename = "Classifier_Data.csv"
csv = np.genfromtxt (filename, delimiter=",")

# Name = csv[:,0]
# Experience = csv[:,1]
# ActualGain = csv[:,2]
#Extracting Training Data and Target Variable From the data
training_data = csv[:,1:3] #Taking only experience and Actual Gain under consideration
target_Felt = csv[:,3] #Extracting target classes
features = ["Experience","Actual Gain"] #Names of features
classes = ["Less","More"] # Names of Target classes
clf = tree.DecisionTreeClassifier()	 # Initiating Decision Tree classifier
clf = clf.fit(training_data,target_Felt) #Training the Decision Tree
test_data_exp = []
test_data_actual_gain = []
while ((test_data_exp!= 'q') | (test_data_actual_gain!= 'q')):
	print("Press q to exit")
	test_data_exp = input("Input the Experience in scale of 0-5: ")
	test_data_actual_gain = input("\n Enter the actual gain applied:")
	print("\nHere is the Prediction")
	test_data = [[test_data_exp,test_data_actual_gain]]
	result = clf.predict(test_data)
	probability = clf.predict_proba(test_data)
	if result ==1:
		print("More with probability ",probability[0][1])
	else:
		print("Less with Probability ",probability[0][0])


#For creating the output pdf from the classifier.
# dot_data = tree.export_graphviz(clf, out_file=None,feature_names=features,class_names=classes,filled= True,rounded= True,special_characters= True) 
# graph = pydotplus.graph_from_dot_data(dot_data) 
# graph.write_pdf("Classifier.pdf") 

