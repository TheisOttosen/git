from sklearn import tree

# Colors as numbers
ColorRed = 0
ColorOrange = 1
ColorYellow = 2
ColorGreen = 3

# Textures as numbers
TextBumpy = 0
TextSmooth = 1
TextHairy = 2

# Stems as numbers
NoStem = 0
Stem = 1

# Fruits as numbers
apple = 0
plum = 1
orange = 2
banana = 3

# Training data
features = [[148, ColorRed, TextSmooth, Stem], [134, ColorRed, TextSmooth, Stem], [137, ColorRed, TextSmooth, Stem], [143, ColorRed, TextSmooth, Stem], [137, ColorRed, TextSmooth, Stem], [87, ColorRed, TextSmooth, NoStem], [77, ColorRed, TextSmooth, NoStem], [83, ColorRed, TextSmooth, NoStem], [177, ColorOrange, TextBumpy, NoStem], [184, ColorOrange, TextBumpy, NoStem], [148, ColorYellow, TextSmooth, Stem], [162, ColorYellow, TextSmooth, Stem], [169, ColorYellow, TextSmooth, Stem]]
labels = [apple, apple, apple, apple, apple, plum, plum, plum, orange, orange, banana, banana, banana]

# Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# Prediction
print(clf.predict([[180, ColorRed, TextBumpy, Stem]]))
