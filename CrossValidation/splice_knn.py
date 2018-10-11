import math
import numpy as np 
import csv


# Calculates distance between v1 and v2
def euclidean(v1,v2):
	d=0.0
	for i in range(len(v1)):
		d+=(float(v1[i])-float(v2[i]))**2
	return math.sqrt(d)

# Gets distance list
def getdistances(data,vec1):
	
	distancelist=[]
	for i in range(len(data)):
		vec2=data[i]
		distancelist.append(euclidean(vec1,vec2))
	return distancelist


# KNN Algorithm
def knn(data,data_y,y_labels,test,k):
	# Gets the distance list
	dis_list=getdistances(data,test)
	# Sort the distance list
	sorted_dis_list=sorted(dis_list)
	
	Dz=[]
	for i in range(k):
		Dz.append(dis_list.index(sorted_dis_list[i]))
	
	vote=[]
	for i in range(len(y_labels)):
		vote.append(0)
		for j in range(len(Dz)):
			# Increment the vote for a class 
			if data_y[Dz[j]]==y_labels[i]:
				vote[i]+=1
	return vote

'''
# Preprocessing
# To Generate Dataset in matrix form
f=open("splice.data","r")

reader=csv.reader(f,delimiter=',')
data=[]
data_y=[]
d={'A':1.0,'T':2.0,'G':3.0,'C':4.0,'N':5.0,'D':6.0,'R':7.0,'S':8.0}

for row in reader:
	s=list(row[2].strip())
	data1=[]
	for i in s:
		if i in d:
			data1.append(d[i])
	data1.append(row[0])
	data.append(data1)
	if row[0] not in data_y:
		data_y.append(row[0])
	
count=0
print data_y
for i in data[1:]:
	vote=knn(data,data_y,i[:-1],1)
	#print data_y[vote.index(max(vote))],i[-1]
	if data_y[vote.index(max(vote))]==i[-1]:
		count+=1

print count,len(data)-1
print float(count)/(len(data)-1)
'''