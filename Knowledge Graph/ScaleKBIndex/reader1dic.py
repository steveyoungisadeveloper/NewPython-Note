# coding: UTF-8
import csv
import pickle

validincluded=0
pred = []
predic={}
ent = []
entdic={}
facttrain=[]
facttest=[]
thefile = open('rdata/fact.csv', 'w', encoding='UTF-8')
with open('2.csv', 'r', encoding='UTF-8') as f:
	reader = csv.reader(f, dialect='excel',delimiter=' ' )
	for objects in reader:
		## print (len(objects))
		if objects[0] not in predic.keys():
			pred.extend([objects[0]])
			predic[objects[0]]=len(pred)-1
			p=predic[objects[0]]
		else:
			p=predic[objects[0]]
		if objects[1] not in entdic.keys():
			ent.extend([objects[1]])
			entdic[objects[1]]=len(ent)-1
			e0=entdic[objects[1]]
		else:
			e0=entdic[objects[1]]
		if objects[2] not in entdic.keys():
			ent.extend([objects[2]])
			entdic[objects[2]]=len(ent)-1
			e1=entdic[objects[2]]
		else:
			e1=entdic[objects[2]]
		facttest.append([p+1,e0+1,e1+1])

for item in facttest:
	newEntry = str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + " "
	thefile.writelines(newEntry + "\n" )

thefile.close()
