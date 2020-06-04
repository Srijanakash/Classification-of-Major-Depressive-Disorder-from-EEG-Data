# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:02:09 2019

@author: Srijan
"""

import numpy as np
import pandas as pd
import warnings
from ant_colony import AntColony
warnings.filterwarnings('ignore')

tdata=pd.read_csv("train_new.csv")
y=tdata['mdd']
x=tdata.iloc[1:66,1:66]
x=np.array(x)
#x=np.transpose(x)

ant_colony = AntColony(x, 50, 10, 100, 0.95, alpha=10, beta=5)
shortest_path = ant_colony.run()
s_path=shortest_path[0]
weight=shortest_path[1]

path=[]

l=len(s_path)
l-=2
print('Shortest Path: ',end='\t')
for i in range(l):
    if(i!=l):
        print(s_path[i][1],end=' -> ')
        path.append('C'+str(s_path[i][1]))
print(s_path[l][1])
path.append('C'+str(s_path[l][1]))
print("\n")
#print ("Shortest Path: {}".format(s_path))
print('Weight: {:.2f}'.format(weight))
