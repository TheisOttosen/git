import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

""" 
# MetaData
print (iris.feature_names)
print (iris.target_names)
print (iris.data[0]) # First line data
print (iris.target[0]) # First line target
"""

test_index = [0,50,100]

train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index)
