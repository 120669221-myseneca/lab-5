#!/usr/bin/env python3
# Author : Prince Dungrani
# Author ID: 120669221
f = open('data.txt', 'r')

def read_file_string(file_name):
    f = open(file_name, 'r')  # Open file in read mode
    read_data = f.read()      # Read entire content as a single string
    f.close()                 # Close file
    return read_data
def read_file_list(file_name):
    f = open(file_name, 'r')  
    method2 = f.readlines()   
    f.close()                 
    return [line.strip() for line in method2]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
