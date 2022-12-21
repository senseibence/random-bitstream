import hashlib
import numpy
from matplotlib import pyplot as plt 
from PIL import Image
import statistics
import random

Random_Numbers = ''
Random_Bits = ''

def generateRandom():
  global Random_Numbers
  global Random_Bits

  # file path syntax makes a hard time for variable insertion, thus two separate code blocks and not a function is used
  for i in range(2, 4981):

    # Open images of pendulum
    if (i < 10): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\00'+str(i)+'.jpg')
    elif (i < 100): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\0'+str(i)+'.jpg')
    else: image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\'+str(i)+'.jpg')

    # Get pixel data
    pixel_array = numpy.array(image.getdata())
    pixel_array = pixel_array.flatten()

    # Hash with SHA-256
    hash_value = hashlib.sha256(pixel_array).hexdigest()

    # Create both random numbers and bits
    random_number = int(hash_value, 16)
    random_bitstream = bin(random_number)[2:]

    Random_Numbers += str(random_number)
    Random_Bits += str(random_bitstream)
  
  for i in range(14, 3801):
    if (i < 10): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures2\\00'+str(i)+'.jpg')
    elif (i < 100): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures2\\0'+str(i)+'.jpg')
    else: image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures2\\'+str(i)+'.jpg')
    pixel_array = numpy.array(image.getdata())
    pixel_array = pixel_array.flatten()
    hash_value = hashlib.sha256(pixel_array).hexdigest()
    random_number = int(hash_value, 16)
    random_bitstream = bin(random_number)[2:]
    Random_Numbers += str(random_number)
    Random_Bits += str(random_bitstream)

generateRandom()

# writing numbers to files
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'w')
random_bits_txt = open('C:\\Users\\bence\\Documents\\Random Bits.txt', 'w')
random_numbers_txt.writelines(Random_Numbers)
random_bits_txt.writelines(Random_Bits)

'''
# reading numbers from file
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'r')
string = random_numbers_txt.read()
convert_to_list = list(string)
'''

# single image that was not parsed earlier will be used as the shuffling seed
image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\001.jpg')

pixel_array = numpy.array(image.getdata())
pixel_array = pixel_array.flatten()
hash_value = hashlib.sha256(pixel_array).hexdigest()
random_number = int(hash_value, 16)
random_bitstream = bin(random_number)[2:]

# shuffle 
Random_Numbers = list(Random_Numbers)
random.seed(random_bitstream)
random.shuffle(Random_Numbers) 

# statistics
frequencies = numpy.array([0,0,0,0,0,0,0,0,0,0])
for digit in Random_Numbers:
  frequencies[int(digit)] += 1

'''
x_axis = (0,1,2,3,4,5,6,7,8,9)
y_axis = frequencies

plt.bar(x_axis, y_axis)
plt.title('frequency vs. digits') 
plt.xlabel('digits')
plt.ylabel('frequency')
plt.show()

plt.bar(x_axis, y_axis)
plt.yscale('log')
plt.title('frequency vs. digits') 
plt.xlabel('digits')
plt.ylabel('frequency')
plt.show()
'''

def sort(list):
  for i in range(len(list)):
    for j in range(len(list)-1):
      first_frequency = list[j]
      second_frequency = list[j+1]
      if second_frequency < first_frequency: 
        list[j] = second_frequency
        list[j+1] = first_frequency
  return list

print(frequencies)
sorted_frequencies = sort(frequencies)
print(sorted_frequencies)
print()

median = statistics.median(sorted_frequencies)
Q1 = numpy.percentile(sorted_frequencies, 25)
Q3 = numpy.percentile(sorted_frequencies, 75)

print("Min: "+str(sorted_frequencies[0]))
print("Q1: "+str(Q1))
print("Median: "+str(median))
print("Q3: "+str(Q3))
print("Max: "+str(sorted_frequencies[-1]))
print()

range = (sorted_frequencies[-1])-(sorted_frequencies[0])
print("Range: "+str(range))
IQR = Q3-Q1
print("IQR: "+str(IQR))

deviation = IQR*1.5
lowest_allowed = Q1-deviation
highest_allowed = Q3+deviation
print("Deviation: "+str(deviation))
print("Lowest Allowed: "+str(lowest_allowed))
print("Highest Allowed: "+str(highest_allowed))
print()

for frequency in sorted_frequencies:
  if (frequency < lowest_allowed): print("Too low: "+str(frequency))
  if (frequency > highest_allowed): print("Too high: "+str(frequency))

# Write to Healey txt
