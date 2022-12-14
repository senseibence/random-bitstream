from PIL import Image
import math
Bitstream = []

# unused function
def roundNumber(number):
  decimal = number - math.floor(number)
  if decimal < 0.5: return math.floor(number)
  return math.ceil(number)

def generateBitstream():
    for i in range(5,125):
        if (i < 10): im = Image.open(r'C:\Users\bence\Pictures\Saved Pictures\FramebyFrame\ezgif-frame-00'+str(i)+'.jpg')
        elif (i < 100): im = Image.open(r'C:\Users\bence\Pictures\Saved Pictures\FramebyFrame\ezgif-frame-0'+str(i)+'.jpg')
        else: im = Image.open(r'C:\Users\bence\Pictures\Saved Pictures\FramebyFrame\ezgif-frame-'+str(i)+'.jpg')
        
        # im.show()

        pixels_of_image = list(im.getdata())

        pixelCount = 0
        sum = 0
        length = 0

        for pixel in pixels_of_image:
            pixelCount += 1
            for colorValue in pixel:
                sum += colorValue
                length += 1

        average = sum/length
        decimalFloat = average - math.floor(average)
    
        decimalString = str(decimalFloat)
        decimalString = decimalString[2:-1]
    
        allDigits = [int(digit) for digit in decimalString]
        
        for i in range(len(allDigits)):
            if (allDigits[i] % 2 == 0): allDigits[i] = 0
            else: allDigits[i] = 1
        
        Bitstream.append(allDigits)

generateBitstream()
Bitstream = [bit for pixel in Bitstream for bit in pixel]
print(''.join(str(bit) for bit in Bitstream)) # '' --> ' ' if you want a space between bits

zeroCount = 0
oneCount = 0
for bit in Bitstream:
    if bit == 0: zeroCount += 1
    elif bit == 1: oneCount += 1

print()
print('# of 0s: '+str(zeroCount))
print('# of 1s: '+str(oneCount))
