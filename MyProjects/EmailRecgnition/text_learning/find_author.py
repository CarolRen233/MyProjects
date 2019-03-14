#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import numpy
numpy.random.seed(42)

'''
    Since we have so many features, we can firstly select the strongest
    feature.
    And then create some classifier to indentify the author
'''

word_data = pickle.load( open("D:/yan/MyProjects/EmailRecgnition/tools/word_data.pkl", "r"))
authors = pickle.load( open("D:/yan/MyProjects/EmailRecgnition/tools/email_authors.pkl", "r") )


### Split dataset into test and train

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)



### Delete Stopwords and do tfidf
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

### we need to know which feature has the largest importance score

words = vectorizer.get_feature_names()

print "We have",len(words),"features"


### print the accuracy score 
from sklearn import tree  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred=clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(labels_test,pred)
print "accuracy:",accuracy


### print a list of feature inportance,so we can see which feature is more important
fi=clf.feature_importances_
 
print "Important features:"
for index, feature in enumerate(clf.feature_importances_):
    if feature>0.2:
        print "feature no", index
        print "importance", feature
        print "word with highest importance is", words[index]





### SVM 

from sklearn import svm
clf=svm.SVC(kernel='rbf',C=1000,gamma='scale')
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
accuracy=accuracy_score(pred,labels_test)
print "Accuracy of identifing author is:",accuracy

