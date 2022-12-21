import hashlib
import numpy
from matplotlib import pyplot as plt 
from PIL import Image
import statistics
import random

Random_Numbers = ''

def generateRandom(list):
  for i in range(2): 
    for j in range(1, list[i]):
      print(j)

      # Open images of pendulum
      if (j < 10): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\00'+str(j)+'.jpg')
      elif (j < 100): image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\0'+str(j)+'.jpg')
      else: image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\'+str(j)+'.jpg')

      # Get all pixel values
      pixel_array = numpy.array(image)
      pixel_array = pixel_array.flatten()

      # Hash with SHA-256
      hash_value = hashlib.sha256(pixel_array).hexdigest()

      # Create both random numbers and bits
      random_number = int(hash_value, 16)

      global Random_Numbers
      Random_Numbers += str(random_number)

# generateRandom([4981, 3801])

# writing numbers to file
'''
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'w')
random_numbers_txt.writelines(Random_Numbers)
'''

# reading numbers from file
random_numbers_txt = open('C:\\Users\\bence\\Documents\\Random Numbers.txt', 'r')
string = random_numbers_txt.read()
convert_to_list = list(string)

# single image that was not parsed earlier will be used as the shuffling seed
image = Image.open(r'C:\\Users\\bence\\Pictures\\Saved Pictures\\acrylicpendulum\\pictures1\\4980.jpg')

pixel_array = numpy.array(image)
pixel_array = pixel_array.flatten()

# any one of the three below could be used as a seed
hash_value = hashlib.sha256(pixel_array).hexdigest()
random_number = int(hash_value, 16)
random_bitstream = bin(random_number)[2:]

# shuffle 
random.seed(random_bitstream)
random.shuffle(convert_to_list) 

# everything below is statistics for the chosen range of [106221:107221]

frequencies = numpy.array([0,0,0,0,0,0,0,0,0,0])
for digit in convert_to_list[106221:107221]:
  frequencies[int(digit)] += 1

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
sorted_counter_array = sort(frequencies)
print(sorted_counter_array)
print()

median = statistics.median(sorted_counter_array)
Q1 = numpy.percentile(sorted_counter_array, 25)
Q3 = numpy.percentile(sorted_counter_array, 75)

print("Min: "+str(sorted_counter_array[0]))
print("Q1: "+str(Q1))
print("Median: "+str(median))
print("Q3: "+str(Q3))
print("Max: "+str(sorted_counter_array[-1]))
print()

range = sorted_counter_array[-1]-sorted_counter_array[0]
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

for frequency in sorted_counter_array:
  if (frequency < lowest_allowed): print("Too low: "+str(frequency))
  if (frequency > highest_allowed): print("Too high: "+str(frequency))
    
# write result list to file
'''
fordeanhealey = open('C:\\Users\\bence\\Documents\\fordeanhealey.txt', 'w')
fordeanhealey.writelines(convert_to_list[106221:107221])
'''
