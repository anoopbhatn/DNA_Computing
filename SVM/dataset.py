# To Generate Dataset in matrix form

import numpy as np 
import csv

f=open("splice.data","r")

d={'T':1.0,'A':2.0,'G':3.0,'C':4.0,'N':2.5,'D':2.0,'R':2.5,'S':3.5}

reader=csv.reader(f,delimiter=',')
data=[]
for row in reader:
	s=list(row[2].strip())
	data1=[]
	for i in s:
		if i in d:
			data1.append(d[i])
		'''
		else:
			print i
			data1.append(5.0)
		'''
	data1.append(row[0])
	data.append(data1)

	
data_list=data
data=np.matrix(data)