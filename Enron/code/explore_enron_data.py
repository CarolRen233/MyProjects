#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

try: 
    import cPickle as pickle #python 2 
except:
    import pickle #python 3

import sys

sys.path.append("D:/yan/Enron Project/")

enron_data = pickle.load(open("D:/yan/Enron Project/dataset/final_project_dataset.pkl", "rb"))


print" Q0:How many data points are in the Enron dataset?"
print "There are ",len(enron_data),"data points in this dataset"
print '------------------------------------------------------------------\n\n'


print "Q1:Print every key in the dictionary  i.e. the index or the staff's names"
print "keys in enron data dictionary", enron_data.keys()
print '------------------------------------------------------------------\n\n'

print "Q2:How many features in one key?"
print enron_data["METTS MARK"].keys()  
count=0
for i in enron_data["METTS MARK"]:
    count+=1
print "There are ",count,"features in one key"

print '------------------------------------------------------------------\n\n'



print " Q3:How many POI(person of interest)in the Enron dataset? "
count=0
for i in enron_data.keys():
    if enron_data[i]["poi"]==1:
	    count+=1

print "There are ",count,"POI in this dataset"
print '------------------------------------------------------------------\n\n'



print " Q4:How many POI we listed?"
f= open('D:/yan/Enron Project/dataset/poi_names.txt')
context=f.readlines()
count=0
for line in context:
    if line.startswith('(y)')==True or line.startswith('(n)')==True:
	    count+=1
		
print "There are ",count,"POIs we listed"
print '------------------------------------------------------------------\n\n'




print "Q5: How much is James Prentice's total stock value? "
print "James Prentice's total stock value is",enron_data["PRENTICE JAMES"]["total_stock_value"]
print '------------------------------------------------------------------\n\n'


print "Q6: How many emails Wesley Colwell sent to poi?"
print "There are ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"],"emails Wesley Colwell sent to poi"
print '------------------------------------------------------------------\n\n'


print "Q7: Who got the most money? How much money was it? "
print "Jeffrey Skilling got",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Kenneth Lay got",enron_data["LAY KENNETH L"]["total_payments"]
print "Andrew Fastow got",enron_data["FASTOW ANDREW S"]["total_payments"]
print '------------------------------------------------------------------\n\n'



print "Q8:How many folks in this dataset have a quantified salary and known email adress? "
count1=0
count2=0
for key in enron_data:
    if enron_data[key]["salary"]!="NaN":
	    count1+=1
	
for key in enron_data:
	if enron_data[key]["email_address"]!="NaN":
	    count2+=1
		
print "There are ",count1,"folks in this dataset have a quantified salary"
print "There are ",count2,"folks in this dataset have a known email adress"

print '------------------------------------------------------------------\n\n'


print "Q9: Print one person's information"

for key in enron_data["LAY KENNETH L"]:
    print key , enron_data["LAY KENNETH L"][key]