import math
import numpy as np

data_file = open("C:/Users/Rachel/CS 170/CS-170-Project-2/CS170_Small_Data__37.txt", "r")
content = data_file.readlines()
number_correctly_classified = 0

for i in range(len(content)):
    row = np.array(content[i].split(), dtype = float) 

    dataset_object_label = content[i].strip() #removes the whitespaces that trail behind the first integer number of every newline
    if not dataset_object_label:
        continue
    dataset_object_label= dataset_object_label[0]
    dataset_object = row[1:]

    nearest_neighbor_distance = float('inf')
    nearest_neighbor_location = float('inf')

    for k in range(len(content)):
        next_row = np.array(content[k].split(), dtype = float)

        other_dataset_object_label = content[k].strip()
        other_dataset_object_label = other_dataset_object_label[0]
        other_dataset_object = next_row[1:]
      

        if k != i:
            a = np.round(np.array(dataset_object),2) #rounds to two decimal places
            b = np.round(np.array(other_dataset_object),2)
            distance = np.sqrt(sum((a - b) ** 2))

            if distance < nearest_neighbor_distance:
                nearest_neighbor_distance = distance
                nearest_neighbor_location = k
                nearest_neighbor_row = content[nearest_neighbor_location]

                nearest_neighbor_label = np.array(nearest_neighbor_row.split())
                nearest_neighbor_label = nearest_neighbor_row.strip()
                nearest_neighbor_label = nearest_neighbor_label[0]

    if dataset_object_label == nearest_neighbor_label:
        number_correctly_classified = number_correctly_classified + 1


print(number_correctly_classified,len(content))

accuracy = number_correctly_classified / (len(content))
print("The accuracy for this data set is:", accuracy)

data_file.close()