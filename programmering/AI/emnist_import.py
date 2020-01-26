# STEP 1.1

# The first thing we're going to do
# is import the EMNIST libraries 
# so that we have access the training set.

# commands
# !git clone https://github.com/sorki/python-mnist
# !./python-mnist/get_data.sh
# !pip3 install emnist

from emnist import extract_training_samples

print ("Imported the EMNIST libraries we need!")





# STEP 1.2

# Grab the data from the OpenML website
# X will be our images and y will be the labels
X, y = extract_training_samples('letters')

# Make sure that every pixel in all of the images is a value between 0 and 1
X = X / 255.

# Use the first 60000 instances as training and the next 10000 as testing
X_train, X_test = X[:60000], X[60000:70000]
y_train, y_test = y[:60000], y[60000:70000]

# There is one other thing we need to do, we need to
# record the number of samples in each dataset and the number of pixels in each image
X_train = X_train.reshape(60000,784)
X_test = X_test.reshape(10000,784)

print("Extracted our samples and divided our training and testing data sets")





# STEP 1.3

import matplotlib.pyplot as plt

img_index = 14000 # <<<<<  You can update this value to look at other images
img = X_train[img_index]
print("Image Label: " + str(chr(y_train[img_index]+96)))
plt.imshow(img.reshape((28,28)))