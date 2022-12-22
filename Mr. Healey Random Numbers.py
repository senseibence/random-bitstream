import hashlib
import numpy
from matplotlib import pyplot as plt 
from PIL import Image
import statistics
import random

Random_Numbers = ''
Random_Bits = ''

# the bits created are not used in this program
def generateRandom(list):
  global Random_Numbers
  global Random_Bits

  for i in range(1,6): 
    i_index = str(i)
    for j in range(1,(list[i-1]+1)): 
      j_index = str(j)

      print(j)
      if (j < 10): filePath = 'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\Double Pendulum '+i_index+'\\00'+j_index+'.jpg'
      elif (j < 100): filePath = 'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\Double Pendulum '+i_index+'\\0'+j_index+'.jpg'
      else: filePath = 'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\Double Pendulum '+i_index+'\\'+j_index+'.jpg'
      
      # Open images of pendulum
      image = Image.open(fp=filePath, mode='r')

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

# 3 helper functions

# bubble sort
def sort(list):
  for i in range(len(list)):
    for j in range(len(list)-1):
      first_frequency = list[j]
      second_frequency = list[j+1]
      if second_frequency < first_frequency: 
        list[j] = second_frequency
        list[j+1] = first_frequency
  return list

# minimum 
def findMinimum(list):
  minimum = 10000000
  for item in list: 
    if item<minimum: 
      minimum=item
  return minimum

# statistics
def statisticalTest():
  # misleading histograms

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

  print(frequencies)
  sorted_frequencies = sort(frequencies)
  print(sorted_frequencies)
  print("# of Rand Nums: "+str(len(all_random_numbers)))
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

  single_range = (sorted_frequencies[-1])-(sorted_frequencies[0])
  print("Range: "+str(single_range))
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

# generateRandom([200, 200, 240, 200, 220])

# writing numbers to files
'''
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'w')
random_bits_txt = open('C:\\Users\\bence\\Documents\\Random Bits.txt', 'w')
random_numbers_txt.writelines(Random_Numbers)
random_bits_txt.writelines(Random_Bits)
'''

# reading numbers from file
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'r')
string = random_numbers_txt.read()
all_random_numbers = list(string)

# option to shuffle data before analyzing frequency
'''
image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\randompics\\japanesewaves.jpg')
pixel_array = numpy.array(image.getdata())
pixel_array = pixel_array.flatten()
hash_value = hashlib.sha256(pixel_array).hexdigest()
random_number = int(hash_value, 16)
random_bitstream = bin(random_number)[2:]

random.seed(hash_value)
random.shuffle(all_random_numbers)
random.seed(random_number)
random.shuffle(all_random_numbers)
random.seed(random_bitstream)
random.shuffle(all_random_numbers)
'''

# finding range of 2800 (one page's worth) numbers with least variance in frequency
'''
range_list = []
for i in range(len(all_random_numbers)-2799): 
  frequencies = [0,0,0,0,0,0,0,0,0,0]
  print(i)
  
  for digit in all_random_numbers[i:(2800+i)]:
    frequencies[int(digit)] += 1
  
  sorted_frequencies = sort(frequencies)
  single_range = (sorted_frequencies[-1])-(sorted_frequencies[0])
  range_list.append(single_range)

minimum = findMinimum(range_list)
index = range_list.index(minimum)
print("lowest range: "+str(minimum))
print("index of range: "+str(index))
'''

# using range from above to get optimal numbers, shuffling using a random image
frequencies = [0,0,0,0,0,0,0,0,0,0]
for digit in all_random_numbers[77023:(2800+77023)]:
  frequencies[int(digit)] += 1

all_random_numbers = all_random_numbers[77023:(2800+77023)]
statisticalTest()

image = Image.open(fp='C:\\Users\\bence\\Pictures\\Saved Pictures\\randompics\\japanesewaves.jpg', mode='r')
image.show()
pixel_array = numpy.array(image.getdata())
pixel_array = pixel_array.flatten()
hash_value = hashlib.sha256(pixel_array).hexdigest()
random_number = int(hash_value, 16)
random_bitstream = bin(random_number)[2:]

# this can be skipped if you mistrust python random, but for shuffling w/ your own seed it is reasonable
random.seed(hash_value)
random.shuffle(all_random_numbers)
random.seed(random_number)
random.shuffle(all_random_numbers)
random.seed(random_bitstream)
random.shuffle(all_random_numbers)

# writing final random numbers to file
result = ''.join(str(num) for num in all_random_numbers)
healey_random_numbers_txt = open('C:\\Users\\bence\\Documents\\Mr Healey Random Numbers.txt', 'w')
healey_random_numbers_txt.writelines(result)
