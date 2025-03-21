import math
import numpy as np
import nearest_neighbor
import search

print("Welcome to Rachel Lee's Feature Selection Algorithm.\n")
file_entered = input("Type in the name of the file to test:\n")
text_file = open(file_entered,'r')
content = text_file.readlines()

print("Type the number of the algorithm you want to run:\n 1) Forward Selection\n 2) Backward Elimination\n")
algorithm_selection = int(input())

if algorithm_selection == 1:
    print("This dataset has")
    print("Beginning search")
    search.search(content)

text_file.close()
