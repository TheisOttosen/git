# importerer biblioteker
import numpy
from skimage import data

camera = data.camera() # laver datasæt til variabel

# tjekker om det virker
print (camera.shape)
print (camera.size)

print (camera.min(), camera.max()) # printer minimums- og maximumsværdi
print (camera.mean())

print (camera)
