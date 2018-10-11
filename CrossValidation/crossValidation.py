import numpy as np 
from sklearn import svm
from sklearn.linear_model import LogisticRegression
import splice_dt
import splice_knn
from sklearn import cross_validation
from dataset import dataset_dt,data_x,data_y


def train_svm(X,Y):
	# An instance of SVM Classifier
	clf = svm.SVC()
	# Fit the data
	clf.fit(X,Y)

	return clf

def train_log_reg(X,Y):

	# An instance of LogisticRegression
	logistic = LogisticRegression()
	# Fit the data
	logistic.fit(X,Y)

	return logistic

def train_decision_tree(X):

	atr=range(len(X[0])-1)
	tree=splice_dt.TreeGrowth(X,atr)

	return tree


def validate_svm_log_reg(clf,X,Y):

	count=0
	tot=0

	for i in range(len(X)):
		tot+=1
		query=np.matrix(X[i])

		# Predict the class label
		res=clf.predict(query)

		if res[0]==Y[i]:
			count+=1

	return (float(count)/tot)*100


def validate_decision_tree(tree,X):

	count=0
	tot=0

	for i in range(len(X)):

		tot+=1

		result=splice_dt.makeDecision(tree,X[i][:-1])

		if result == X[i][-1]:
			count+=1

	return (float(count)/tot)*100

def validate_knn(X,Y,testX,testY):

	y_labels=[]
	for i in Y:
		if i not in y_labels:
			y_labels.append(i)

	count=0
	tot=0

	for i in range(len(testX)):

		tot+=1

		vote=splice_knn.knn(X,Y,y_labels,testX[i],5)

		if y_labels[vote.index(max(vote))] == testY[i]:
			count+=1

	return (float(count)/tot)*100


kf_total = cross_validation.KFold(len(dataset_dt), n_folds=10, shuffle=True, random_state=4)

fold=1

foldList=[]
dtList=[]
knnList=[]
logRegList=[]
svmList=[]

fh=open('result.csv','w')

for train, test in kf_total:
	
	train_dt=[]
	train_other_x=[]
	train_other_y=[]

	test_dt=[]
	test_other_x=[]
	test_other_y=[]

	for i in train:
		train_dt.append(dataset_dt[i])

		train_other_x.append(data_x[i])
		train_other_y.append(data_y[i])


	for i in test:
		test_dt.append(dataset_dt[i])

		test_other_x.append(data_x[i])
		test_other_y.append(data_y[i])

	dt=train_decision_tree(train_dt)

	knn_res=validate_knn(train_other_x,train_other_y,test_other_x,test_other_y)

	train_other_x=np.matrix(train_other_x)
	
	logreg=train_log_reg(train_other_x,train_other_y)

	svm1=train_svm(train_other_x,train_other_y)

	dt_res=validate_decision_tree(dt,test_dt)

	log_res=validate_svm_log_reg(logreg,test_other_x,test_other_y)

	svm_res=validate_svm_log_reg(svm1,test_other_x,test_other_y)

	print 'Fold : ',fold,' dt : ',dt_res,' , logreg : ',log_res,' , svm : ',svm_res,' , knn : ',knn_res

	sw='Fold : '+str(fold)+' , dt : '+str(dt_res)+' , logreg : '+str(log_res)+' , svm : '+str(svm_res)+' , knn : '+str(knn_res)
	fh.write(sw)

	foldList.append(fold)
	dtList.append(dt_res)
	knnList.append(knn_res)
	logRegList.append(log_res)
	svmList.append(svm_res)

	fold+=1


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

# Plotting accuracies of different classifiers for whole training data

x=[0,2,5,8,11]
classifiers=['','Decision Tree','Logistic Regression','KNN','SVM']
accuracies=[0,81.73,73.98,72.18,97.62]

plt.axis((0,12,60,120))
plt.xticks(x,classifiers)
plt.plot(x,accuracies,'bo')
plt.show()

# Plotting accuracies of different classifiers for Cross Validation

dtLine, = plt.plot(foldList,dtList,'r',label='Decision Tree')
logRegLine, = plt.plot(foldList,logRegList,'b',label='Logistic Regression')
knnLine, = plt.plot(foldList,knnList,'g',label='KNN')
svmLine, = plt.plot(foldList,svmList,'k',label='SVM')

plt.legend([dtLine,logRegLine,knnLine,svmLine],['Decision Tree','Logistic Regression','KNN','SVM'],loc=4)

plt.show()



