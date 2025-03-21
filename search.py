import random
import numpy as np
from nearest_neighbor import leave_one_out_cross_validation

def search(content):
    column_of_labels = []
    column_of_features = []
    current_set_of_features = set()

    new_content = []
    for x in content:  #seperates all the information in the txt file into float elements within a row
        row = x.strip().split()
        row = [float(element) for element in row]
        new_content.append(row)
        column_of_labels.append(row[0]) #only the 0th element/class label of every row
        column_of_features.append(row[1:]) #the features for every row

    number_of_features = len(new_content[0]) - 1 

    for level in range(1,number_of_features + 1):
        best_so_far_accuracy = 0
        print("On the", level,"th level of the search tree")
        print("current set of features at level", level, ":", current_set_of_features)
        feature_to_add_at_this_level = None

        for column_number in range(1, number_of_features + 1):
            if column_number not in current_set_of_features:
                accuracy = leave_one_out_cross_validation(new_content,current_set_of_features,column_number)
        
                print("Using feature(s) {", column_number, "} accuracy is",f"{accuracy * 100:.1f}%") #accuracy is converted from a decimal into a percentage

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = column_number

        if feature_to_add_at_this_level is not None:
            current_set_of_features.add(feature_to_add_at_this_level)
            accuracy = leave_one_out_cross_validation(new_content, current_set_of_features, column_number)
        

        print("Feature set",current_set_of_features,"was best, accuracy is", f"{accuracy * 100:.1f}%")
    
    print("Finished search! The best feature subset is {", "which has an accuracy of")
