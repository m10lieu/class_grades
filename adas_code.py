
def read_data(infile):
    
    import numpy as np
    columns= np.loadtxt(infile,delimiter=',',skiprows=0,unpack=True)
    grade_column= columns[1]
    return columns, grade_column


    
    
    
    



    
