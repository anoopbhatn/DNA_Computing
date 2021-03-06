
import numpy as np 
from sklearn.neural_network import MLPClassifier
from dataset import data,data_list
import pickle

# Extract only attribute information from data
x=data[:,:len(data_list[0])-1]

x=np.array(x)

# List to store converted float values for the attributes
x1=[]
# Getting values in float
for i in range(len(x)):
	x1.append([])
	for j in range(len(x[0])):
		x1[i].append(float(x[i][j]))

# Matrix of values of all 4 attributes
x=np.matrix(x1)

y=[]
# Matrix of all the class labels for all records
for i in data_list:
	y.append(i[-1])

count=0
tot=0

mlp_f = open("svm.pickle", "rb")
mlp = pickle.load(mlp_f)
mlp_f.close()

for i in data_list:
	tot+=1

	query=i[:-1]
	query=np.matrix(query)


	# Predict the class label
	res=mlp.predict(query)

	if res[0]==i[-1]:
		count+=1
accuracy=(float(count)/tot)*100

print 'Accuracy : ',accuracy,'%'
