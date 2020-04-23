# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:26:06 2019

@author: Srijan
"""

import csv
from collections import defaultdict
import numpy as np
import pywt
from scipy.signal import *
from numpy.fft import * 
from scipy import *
from pylab import *
import warnings
warnings.filterwarnings('ignore')



fout_data = open("Train.csv",'a')


for i in range (507,629):
    if i!=544 and i!=571 and i!=572:
        vec = []
        filename=str(i)+".csv"
        print(filename)
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            #print(type(row1))
            print(len(row1))
            columns = defaultdict(list) # each value in each column is appended to a list
            rows=[]
            with open(filename) as f:
                reader = csv.DictReader(f) # read rows into a dictionary format
                for row in reader: # read a row as {column1: value1, column2: value2,...}
                    for (k,v) in row.items():
                        if v!="":    
                            columns[k].append(v)
          
            for i in list(columns.keys()):
                x=np.array(columns[i]).astype(np.float)
                coeffs=pywt.wavedec(x,'db4',level=6)
                cA6,cD6,cD5,cD4,cD3,cD2,cD1=coeffs
                cD5=np.std(cD5)
                cD4=np.std(cD4)
                cD3=np.std(cD3)
                cD2=np.std(cD2)
                cD1=np.std(cD1)
                fout_data.write(str(cD5)+",")
                fout_data.write(str(cD4)+",")
                fout_data.write(str(cD3)+",")
                fout_data.write(str(cD2)+",")
                fout_data.write(str(cD1)+",")
        fout_data.write("\n")
        print(filename+" finished")
            
fout_data.close()
