import numpy as np

def read_data(infile):
    columns= np.loadtxt('infile',delimiter=',',skiprows=0,unpack=True)
    grade_column= columns[1]
    return columns, grade_columns


    
    
    
    



    
