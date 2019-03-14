#!/usr/bin/python

import sys
import pickle
import numpy as np
sys.path.append("D:/yan/EnronProject/tools/")
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data



### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_stock_value','long_term_incentive','to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi'] # You will need to use more features


### Load the dictionary containing the dataset
with open("D:/yan/EnronProject/dataset/final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

    
    
    
### Task 2: Remove outliers

import matplotlib.pyplot
import seaborn as sns
data_dict.pop('TOTAL')
data = featureFormat(data_dict, features_list)

for point in data:
    salary = point[1]
    bonus = point[2]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#find the one with the highest salary or bonus
for item in data_dict:
    if data_dict[item]['bonus']!='NaN' and data_dict[item]['salary']!='NaN':
	    if data_dict[item]['bonus']>5e6 and data_dict[item]['salary']>1e6:
		    print 'the one with the highest salary or bonus is:',item


### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
### Create 2 new features:to_messages_ratio and from_messages_ratio
my_dataset = data_dict

for person in my_dataset:
    if my_dataset[person]['to_messages']=='NaN' or my_dataset[person]['from_poi_to_this_person']=='NaN':
        my_dataset[person]['to_poi_ratio']=0.
    else:
        my_dataset[person]['to_poi_ratio']=float(my_dataset[person]['from_poi_to_this_person'])/float((my_dataset[person]['to_messages']))
        

for person in my_dataset:
    if my_dataset[person]['from_messages']=='NaN' or my_dataset[person]['from_this_person_to_poi']=='NaN':
        my_dataset[person]['from_poi_ratio']=0.
    else:
        my_dataset[person]['from_poi_ratio']=float(my_dataset[person]['from_this_person_to_poi'])/float((my_dataset[person]['from_messages']))


features_list = ['poi','salary','bonus','long_term_incentive','total_stock_value','to_poi_ratio','from_poi_ratio']


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)

labels, features = targetFeatureSplit(data)

### Task 4: Split the data and use different classifiers

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42)


# naive_bayes
from sklearn.naive_bayes import GaussianNB
clf1 = GaussianNB()
clf1.fit(features_train,labels_train)
pred=clf1.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(pred,labels_test)

print "Accuracy of naive_bayes is :",accuracy


# SVM

from sklearn import svm
from sklearn.model_selection import GridSearchCV

clf2=svm.SVC(kernel='rbf',C=10,gamma='scale')
clf2.fit(features_train,labels_train)
pred=clf2.predict(features_test)
accuracy=accuracy_score(pred,labels_test)
print "Accuracy of SVM is:",accuracy

# Decision Tree

from sklearn import tree
clf3 = tree.DecisionTreeClassifier(min_samples_split=2)
clf3.fit(features_train, labels_train)

pred=clf3.predict(features_test)

accuracy=accuracy_score(pred,labels_test)
print "Accuracy of Decision Tree is",accuracy



# SVM after GridSearchCV
#parameters = {'kernel':('linear', 'rbf'), 'C':[5, 100]}
#svr = svm.SVC()
#clf4 = GridSearchCV(svr, parameters,cv=5)
#clf4.fit(features_train,labels_train)

#pred=clf4.predict(features_test)
#accuracy=accuracy_score(pred,labels_test)
#print "Accuracy of SVM after GridSearchCV is:",accuracy



