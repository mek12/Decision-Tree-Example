# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:31:38 2019

@author: Emir
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv("decision-tree-regression-dataset.csv", sep=";",header=None)

x=df1.iloc[:,0].values.reshape(-1,1)
y=df1.iloc[:,1].values.reshape(-1,1)


#decision tree
from sklearn.tree import DecisionTreeRegressor
tree_reg=DecisionTreeRegressor()
tree_reg.fit(x,y)

y_head=tree_reg.predict(x)
#visualize

plt.scatter(x,y,color="red")
plt.plot(x,y_head,color="green")
plt.xlabel("tribün level")
plt.ylabel("ucret")
plt.show()