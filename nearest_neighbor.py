import math
import numpy as np

def leave_one_out_cross_validation(content,current_set,feature_to_add):
    number_correctly_classified = 0

    for i in range(len(content)):
        dataset_object_label = content[i][0]
        dataset_object = np.array(content[i][1:])

        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')

        for k in range(len(content)):
            if k != i:
                other_dataset_object_label = content[k][0]
                other_dataset_object = np.array(content[k][1:])

                indexed_feature_to_add = feature_to_add - 1  #makes sure indexing stays consistent between search and nearest neighbor
                indexed_current_set = {index - 1 for index in current_set}

                chosen_features = list(indexed_current_set) + [indexed_feature_to_add]

                filtered_a = dataset_object[chosen_features]
                filtered_b = other_dataset_object[chosen_features]

                distance = np.linalg.norm(filtered_a - filtered_b) #calculates the euclidean distance
                rounded_distance = np.round(distance, 2)

                if rounded_distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = rounded_distance
                    nearest_neighbor_location = k
                    nearest_neighbor_row = content[nearest_neighbor_location]
                    nearest_neighbor_label = nearest_neighbor_row[0]

        if dataset_object_label == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1

    accuracy = number_correctly_classified / (len(content))

    return accuracy
