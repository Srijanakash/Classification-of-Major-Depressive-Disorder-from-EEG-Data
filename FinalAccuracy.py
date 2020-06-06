# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:32:25 2019

@author: Srijan
"""

import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')

tdata=pd.read_csv("train_importance_new_1.csv")
y=tdata['mdd']
x_data=tdata.drop('mdd',axis=1).drop('sub',axis=1)
#x_data.info()


tsize=0.20
X_train, X_test, y_train, y_test = train_test_split(x_data, y, test_size=tsize, random_state=66)


#SVM
svc=SVC(C=100)
svc.fit(X_train,y_train)
print("SVM Accuracy on Test Set: {:.2f}%".format(math.ceil(svc.score(X_test,y_test)*100)))


#Knn
n=1
scores=0
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1,20 )
for n_neighbors in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    temp=knn.score(X_test,y_test)
    if temp>scores:
        n=n_neighbors
        scores=knn.score(X_test,y_test)
    training_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test, y_test))


knn = KNeighborsClassifier(n_neighbors=n)
knn.fit(X_train, y_train)
print("KNN Accuracy on Test Set: {:.2f}%".format(math.ceil(knn.score(X_test, y_test)*100)))

y_pred=knn.predict(X_test)
MSE = np.square(np.subtract(y_test,y_pred)).mean()
print("MSE: {:.2f}".format(MSE))



