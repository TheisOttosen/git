import numpy # værktøj til at have billeder i variabler
from scipy import misc # værktøj til at importere billeder
from sklearn import tree # algoritme

print ("forbereder") # forbereder lister:
features = []
labels = []

frugter = 2
for mappe in range(frugter):
    if (mappe + 1 == 1):
        for foto in range(2):
            features.append([misc.imread("scikit-learn/1/" + str(foto + 1) + ".jpg")])
            labels.append([1])
    if (mappe + 1 == 2):
        for foto in range(2):
            features.append([misc.imread("scikit-learn/2/" + str(foto + 1) + ".jpg")])
            labels.append([2])

# lav og træn classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#classificer ny fugt
print (clf.predict([misc.imread("scikit-learn/test.jpg")]))
