import numpy
from scipy import misc

face = misc.face() # importerer billede

misc.imsave('numpy-images/face.jpg', face) # laver jpg fil
face = misc.imread('numpy-images/face.jpg') # læser jpg fil
