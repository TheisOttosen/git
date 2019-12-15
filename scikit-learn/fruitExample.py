#import
from sklearn import tree

#variabler for tekstur
smooth = 1
bumpy = 2

#variabler for hvilken frugt
apple = 1
orange = 2

#lister med oplysninger og hvad frugten er
features = [[140, smooth], [130, smooth], [150, bumpy], [170,bumpy]]
labels = [apple, apple, orange, orange]

#lav og træn classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#classificer ny fugt
print (clf.predict([[160, bumpy]]))
