# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:49:29 2020

@author: geea
"""
import numpy as np
import pandas as pd

file_name = input("Please enter file name:")
# test_mode = input("Please enter 1 for lateral bending, 2 for torsion or 3 for flexion or extension")

# if test_mode == 1 or test_mode ==2 or test_mode == 3 :
#     pass
# else:
#     test_mode = input("Wrong input please enter 1 for lateral bending, 2 for torsion or 3 for flexion or extension")

file_object = open(file_name, "r")

x_string = []
split_strings = []

for i, line in enumerate(file_object):
    if i > 15 and i < 26:
        x_string.append(line)
        # x[i-16] = line      
    elif i > 25:
      break

print(x_string)

for i, line in enumerate(x_string):
    split_strings.append(line.split())
    split_strings[i].pop(0)
    
print(split_strings)

string_array = np.array(split_strings).astype(np.float)
string_df = pd.DataFrame(data=string_array, columns=["Node","x","y","z","x'","y'","z'"])
string_df.sort_values(by=["z"], inplace=True, ascending=False)
string_df = string_df.reset_index(drop=True)
print(string_df)

for index, rows in string_df.iterrows():
    if index % 2 == 0:
        if string_df.iloc[index,1] < string_df.iloc[index+1,1]:
            a, b = string_df.iloc[index].copy(), string_df.iloc[index+1].copy()
            string_df.iloc[index], string_df.iloc[index+1] = b, a
  
print(string_df)
# for i, line in enumerate(x):
#     y[i] = x.split("")

# print(y)