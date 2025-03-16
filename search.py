import random
import numpy as np

def leave_one_out_cross_validation(content, current_set,feature_to_add):
    accuracy = random.random()
    return accuracy

data_file = open("C:/Users/Rachel/CS 170/CS-170-Project-2/CS170_Small_Data__37.txt", "r")
content = data_file.readlines()

current_set_of_features = set()

column_of_labels = []
column_of_features = []
for x in content:
    row = x.strip().split()
    column_of_labels.append(row[0]) #only the 0th element/class label of every row
    column_of_features.append(row[1:]) #the features for every row

# print(len(column_of_features[0])) #prints out the length of the number of items in the list which is part of the bigger list of all features


for i in range(len(column_of_features)):
    print("On the", i+1,"th level of the search tree")
    feature_to_add_at_this_level = set()
    best_so_far_accuracy = 0

    for k in range(len(column_of_features)):
        if k + 1 not in current_set_of_features:
            print("--Considering adding the", k+1, "feature")
            accuracy = leave_one_out_cross_validation(content,current_set_of_features,k+1)
            if accuracy > best_so_far_accuracy: #only adds the feature if it has not already been added to the set
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level = k+1

    current_set_of_features.add(feature_to_add_at_this_level)
    print("On level", i+1, "I added feature", feature_to_add_at_this_level, "to current set")