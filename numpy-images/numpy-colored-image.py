# importerer biblioteker
import numpy
from skimage import data

cat = data.chelsea() # laver datasæt til variabel

# tjekker om det virker
print (cat.shape)
print (cat.size)

print (cat.min(), cat.max()) # printer minimums- og maximumsværdi
print (cat.mean()) # printer gennemsnittet

print (cat)
