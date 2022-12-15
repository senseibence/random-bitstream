import hashlib
import numpy
from PIL import Image

# Open the image and convert it to grayscale
im = Image.open('C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\IMG_1042\\001.jpg')

# im.show()

# Convert the image to a numpy array
im_array = numpy.array(im)

# Reshape the array to a single dimension
im_array = im_array.flatten()

# Apply the SHA-256 hash function to the pixel values
hash_value = hashlib.sha256(im_array).hexdigest()

# Use the hash value as a random number
random_number = int(hash_value, 16)
random_bitstream = bin(random_number)[2:]

string = str(random_bitstream)

zerocount = 0
onecount = 0

for digit in string:
  if (digit == '0'): zerocount+=1
  elif (digit == '1'): onecount+=1

print("Zero count: "+str(zerocount)+'\n'+"One Count: "+str(onecount))
