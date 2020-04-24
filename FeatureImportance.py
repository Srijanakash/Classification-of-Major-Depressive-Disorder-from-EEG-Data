# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:31:47 2019

@author: Srijan
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tdata=pd.read_csv("train_new.csv")
y=tdata['mdd']
x_data=tdata.drop('mdd',axis=1).drop('sub',axis=1)

tsize=0.20
X_train, X_test, y_train, y_test = train_test_split(x_data, y, test_size=tsize, random_state=66)

#Random Forest
rf=RandomForestClassifier(n_estimators=1000,max_depth=10,random_state=47)
rf.fit(X_train,y_train)
print("Random Forrest Accuracy on Test Set: {:.2f}%".format(rf.score(X_test,y_test)*100))


beta=[]
alpha=[]
theta=[]
delta=[]
gamma=[]

importance=list(rf.feature_importances_)
l=len(importance)
for i in range (0,l):
    temp= i%5
    if(i==0):
        gamma.append(importance[i])
    elif (i==1):
        beta.append(importance[i])
    elif (i==2):
        alpha.append(importance[i])
    elif (i==3):
        theta.append(importance[i])
    elif(i==4):
        delta.append(importance[i])
        
gamma=np.array(gamma)
beta=np.array(beta)
alpha=np.array(alpha)
theta=np.array(theta)
delta=np.array(delta)

gamma_sum=np.sum(gamma)
beta_sum=np.sum(beta)
alpha_sum=np.sum(alpha)
theta_sum=np.sum(theta)
delta_sum=np.sum(delta)

left=[]
for i in range(1,6):
    left.append(i)
#left=[1,2,3,4,5]
graphx=['Gamma','Beta','Alpha','Theta','Delta']
graphy=[gamma_sum,beta_sum,alpha_sum,theta_sum,delta_sum]
plt.plot(left,graphy,'bo-')
plt.bar(left,graphy,tick_label=graphx,width=0.6,color='white')
plt.xlabel('Frequency Band')
plt.ylabel('Importance')
plt.grid()
plt.title('Importance of Frequency Bands')
top1=[0.001,0.002,0.003,0.004,0.005,0.006]
plt.yticks(top1,color='black',rotation=0,fontsize='12')
plt.show()

#plotting feature Importance of Random Forest
importance=list(rf.feature_importances_)
electrode_importance=[]

for i in range (0,len(importance)-4,5):
    avg=-0
    for j in range(i,i+5):
        avg+=importance[i]
    avg=avg/5
    electrode_importance.append(avg)
    
elec_dict={}
for i in range(len(electrode_importance)):
    temp="E"+str(i+1)
    elec_dict[temp]=electrode_importance[i]


elec_dict1=dict(sorted(elec_dict.items(), reverse=True,key = lambda kv:(kv[1], kv[0])))


graphx=[]
graphy=[]
t=0
for i in elec_dict1:
   if(t==15):
       break
   graphx.append(i)
   graphy.append(elec_dict1[i])
   t+=1

left1=[]
for i in range(1,16):
    left1.append(i)

plt.figure(figsize=(10,6))
plt.plot(left1,graphy,'bo-')
plt.bar(left1, graphy, tick_label = graphx, width = 0.6,color='white')
plt.xlabel('Electrode')  
plt.ylabel('Importance') 
plt.grid()
top2=[0.002,0.004,0.006,0.008,0.010]
plt.yticks(top2,color='black',rotation=0,fontsize='12')
plt.title('Feature Importance of Random Forest') 
plt.show

