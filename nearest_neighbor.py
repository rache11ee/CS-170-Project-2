import math

data_file = open("C:/Users/Rachel/CS 170/CS-170-Project-2/CS170_Small_Data__37.txt", "r")
content = data_file.readlines()

for i in range(len(content)):
    row = content[i].strip() #removes the whitespaces that trail behind the first integer number of every newline

    dataset_object = row[1:]
    dataset_object_label = row[0]
 
    # print("At i's location of", i+1)
    # print("The", i+1, "object is in class", dataset_object_label)

    nearest_neighbor_distance = float('inf')
    nearest_neighbor_location = float('inf')

    for k in range(len(content)):
        next_row = content[k].strip()

        other_dataset_object = next_row[1:]
        other_dataset_object_label = next_row[0] #the class of the object following i
        print("Ask if", i+1, "is nearest neighbor with ", k+1)

        if k != i:
            distance = math.sqrt(sum(((dataset_object) - (other_dataset_object))) ** 2)


    #         if distance < nearest_neighbor_distance:
    #             nearest_neighbor_distance = distance
    #             nearest_neighbor_location = k
    #             nearest_neighbor_label = content(nearest_neighbor_location, 1)

    # print("Object", i+1, "is class", dataset_object_label)
    # print("It's nearest neighbor is", nearest_neighbor_location, "which is in class", nearest_neighbor_label)
            




