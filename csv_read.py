import os
import csv
import numpy as np

Input_file_direction=r'C:\Users\Raywang\Desktop\new'
File_number_name=os.listdir(Input_file_direction)
print("File_number_name=",File_number_name)
IN_my_array = np.zeros((1323, len(File_number_name)), float)  #存入矩陣大小
F=open(os.path.join(Input_file_direction,File_number_name[0]),'r')
File=csv.reader(F)
for index,value in enumerate(File):
    IN_my_array[index]= float(value[1])
print(IN_my_array)