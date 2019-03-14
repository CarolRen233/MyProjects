
import sys
import pickle
sys.path.append("D:/yan/EnronProject/tools/")


from feature_format import featureFormat, targetFeatureSplit
features_list = ['poi','salary','bonus','total_stock_value','to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi']


with open("D:/yan/EnronProject/dataset/final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

my_dataset = data_dict


        
        
for person in my_dataset:
    if my_dataset[person]['to_messages']=='NaN' or my_dataset[person]['from_poi_to_this_person']=='NaN':
        my_dataset[person]['to_messages_ratio']=0.
    else:
        my_dataset[person]['to_messages_ratio']=float(my_dataset[person]['from_poi_to_this_person'])/float((my_dataset[person]['to_messages']))
        

for person in my_dataset:
    if my_dataset[person]['from_messages']=='NaN' or my_dataset[person]['from_this_person_to_poi']=='NaN':
        my_dataset[person]['from_messages_ratio']=0.
    else:
        my_dataset[person]['from_messages_ratio']=float(my_dataset[person]['from_this_person_to_poi'])/float((my_dataset[person]['from_messages']))




