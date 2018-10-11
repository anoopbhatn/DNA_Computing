import csv


fileh=open('splice.data','r')

dataset_dt=list()

reader = csv.reader(fileh, delimiter=',')

for row in reader:
	split_row=[]
	s=row[2]
	s=s.strip()
	var=list(s)
	var.append(row[0])
	
	dataset_dt.append(var)


d={'T':1.0,'A':2.0,'G':3.0,'C':4.0,'N':2.5,'D':2.0,'R':2.5,'S':3.5}

fileh=open('splice.data','r')
reader = csv.reader(fileh, delimiter=',')

data_x=[]
data_y=[]

for row in reader:
	s=list(row[2].strip())
	data1=[]
	for i in s:
		if i in d:
			data1.append(d[i])
		
	data_y.append(row[0])
	data_x.append(data1)
	


