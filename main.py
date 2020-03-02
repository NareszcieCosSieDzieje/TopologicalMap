import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

map_width = 0
map_height = 0
adjacent_distance_cm = 0
#data_matrix = list(list())
data_matrix = list()

def hsv2rgb(H, S, V): #0-360, 0-1, 0-1
    RGB = list()
    if H == 360:
        H = 0
    else:
        H/=60.0
    fract = H - math.floor(H)
    P = V * (1. - S)
    Q = V * (1. - S * fract)
    T = V * (1. - S * (1. - fract))
    if (0. <= H) and (H < 1.):
        RGB = [V, T, P]
    elif (1. <= H) and (H < 2.):
        RGB = [Q, V, P]
    elif (2. <= H) and (H < 3.):
        RGB = [P, V, T]
    elif (3. <= H) and (H < 4.):
        RGB = [P, Q, V]
    elif (4. <= H) and (H < 5.):
        RGB = [T, P, V]
    elif (5. <= H) and (H < 6.):
        RGB = [V, P, Q]
    else:
        RGB = [0., 0., 0.]
    return RGB


with open("data.txt", 'r') as file:
    firstLine = file.readline().strip("\n ").split(' ')
    print(firstLine)
    firstLine = [int(i) for i in firstLine]
    map_width = firstLine[0]
    map_height = firstLine[1]
    adjacent_distance_cm = firstLine[2]
    for line in file:
        line = [float(f) for f in line.strip("\n ").split(' ')]
        data_matrix.extend(line)


minl = round((min(data_matrix)),1)
maxl = round((max(data_matrix)),1)
height_range = round(maxl - minl, 1)


pixels = list()

lastv = 0.5 # co 500 zeruj?
satur = -0.5

for v in data_matrix:
    x = (v-minl) / height_range
    rgb = list()
    if x < lastv:
        satur = 0.1
    else:
        satur = 0.
    lastv = x
    if x < 0.05:
        rgb = [120,0.6, 1.0]
    elif x < 0.1:
        rgb = [120, 0.65, 1.0]
    elif x < 0.15:
        rgb = [120, 0.75, 1.0]
    elif x < 0.2:
        rgb = [120, 0.85, 1.0]
    elif x < 0.25:
        rgb = [120, 0.90, 1.0]
    elif x < 0.3:
        rgb = [120, 0.95, 1.0]
    elif x < 0.35:
        rgb =[60, 0.6, 1.0]
    elif x < 0.4:
        rgb =[60, 0.7, 1.0]
    elif x < 0.45:
        rgb =[60, 0.8, 1.0]
    elif x < 0.5:
        rgb =[60, 0.9, 1.0]
    elif x < 0.55:
        rgb =[45, 0.5, 1.0]
    elif x < 0.6:
        rgb = [35, 0.8, 1.0]
    elif x < 0.65:
        rgb =[35, 0.9, 1.0]
    elif x < 0.7:
        rgb =[35, 1.0, 1.0]
    elif x < 0.75:
        rgb = [20, 0.8, 1.0]
    elif x < 0.8:
        rgb =[20, 0.9, 1.0]
    elif x < 0.85:
        rgb =[5, 0.8, 1.0]
    elif x < 0.9:
        rgb =[5, 0.85, 1.0]
    elif x < 0.95:
        rgb = [5, 0.9, 1.0]
    else:
        rgb = [5, 0.95, 1.0]
    rgb[2] -= satur
    rgb[1] += (satur)
    pixels.append(hsv2rgb(rgb[0],rgb[1],rgb[2]))


'''
for v in data_matrix:
    x = (v-minl) / height_range
    rgb = list()
    if x-lastv > 0.4:
        satur += 0.1
    elif lastv-x > 0.4:
        satur = -0.1
    lastv = x
    if satur > 1.0:
       satur = 1.0
    elif satur < 0.4:
       satur = 0.4
    if x < 0.05:
        rgb = [120,0.20,1.0]
    elif x < 0.1:
        rgb = [120, 0.25, 1.0]
    elif x < 0.15:
        rgb = [120, 0.30, 1.0]
    elif x < 0.2:
        rgb = [120, 0.35, 1.0]
    elif x < 0.25:
        rgb = [120, 0.40, 1.0]
    elif x < 0.3:
        rgb = [120, 0.45, 1.0]
    elif x < 0.35:
        rgb =[60, 0.6, 1.0]
    elif x < 0.4:
        rgb =[60, 0.7, 1.0]
    elif x < 0.45:
        rgb =[60, 0.8, 1.0]
    elif x < 0.5:
        rgb =[60, 0.9, 1.0]
    elif x < 0.55:
        rgb =[45, 0.5, 1.0]
    elif x < 0.6:
        rgb = [35, 0.8, 1.0]
    elif x < 0.65:
        rgb =[35, 0.9, 1.0]
    elif x < 0.7:
        rgb =[35, 1.0, 1.0]
    elif x < 0.75:
        rgb = [20, 0.8, 1.0]
    elif x < 0.8:
        rgb =[20, 0.9, 1.0]
    elif x < 0.85:
        rgb =[5, 0.75, 1.0]
    elif x < 0.9:
        rgb =[5, 0.8, 1.0]
    elif x < 0.95:
        rgb = [5, 0.85, 1.0]
    else:
        rgb = [5, 0.9, 1.0]
    rgb[2] = satur
    pixels.append(hsv2rgb(rgb[0],rgb[1],rgb[2]))
'''

'''for v in data_matrix:
    x = (v-minl) / height_range
    if x < 0.05:
        pixels.append(hsv2rgb(120,0.20,1.0))
    elif x < 0.1:
        pixels.append(hsv2rgb(120, 0.25, 1.0))
    elif x < 0.15:
        pixels.append(hsv2rgb(120, 0.30, 1.0))
    elif x < 0.2:
        pixels.append(hsv2rgb(120, 0.35, 1.0))
    elif x < 0.25:
        pixels.append(hsv2rgb(120, 0.40, 1.0))
    elif x < 0.3:
        pixels.append(hsv2rgb(120, 0.45, 1.0))
    elif x < 0.35:
        pixels.append(hsv2rgb(60, 0.6, 1.0))
    elif x < 0.4:
        pixels.append(hsv2rgb(60, 0.7, 1.0))
    elif x < 0.45:
        pixels.append(hsv2rgb(60, 0.8, 1.0))
    elif x < 0.5:
        pixels.append(hsv2rgb(60, 0.9, 1.0))
    elif x < 0.55:
        pixels.append(hsv2rgb(45, 0.5, 1.0))
    elif x < 0.6:
        pixels.append(hsv2rgb(35, 0.8, 1.0))
    elif x < 0.65:
        pixels.append(hsv2rgb(35, 0.9, 1.0))
    elif x < 0.7:
        pixels.append(hsv2rgb(35, 1.0, 1.0))
    elif x < 0.75:
        pixels.append(hsv2rgb(20, 0.8, 1.0))
    elif x < 0.8:
        pixels.append(hsv2rgb(20, 0.9, 1.0))
    elif x < 0.85:
        pixels.append(hsv2rgb(5, 0.75, 1.0))
    elif x < 0.9:
        pixels.append(hsv2rgb(5, 0.8, 1.0))
    elif x < 0.95:
        pixels.append(hsv2rgb(5, 0.85, 1.0))
    else:
        pixels.append(hsv2rgb(5, 0.9, 1.0))'''

pixel_array = list()
for row in range(0,500):
    rowlist = list()
    for col in range(0, 500):
        rowlist.append(pixels[row*500 + col])
    pixel_array.append(rowlist)


fig, ax = plt.subplots()
im = ax.imshow(pixel_array, interpolation='nearest')

plt.show()

'''
for ind, line in enumerate(pixels):
    plt.imshow(line, interpolation='nearest')
    plt.xticks(0, len(line), step=1)
    plt.yticks(ind)
plt.show()



chart = plt.figure(figsize=(20, 20))
chart, ax_lst = plt.subplots(1,1)

for data in data_matrix:
    ax_lst[0].plot( [val for val in data])


plt.imshow(data, interpolation='nearest')
plt.xticks(np.arange(0.0, 2.5, 1), np.arange(0.5, 2, 0.5))
plt.yticks(np.arange(2, -0.5, -1), np.arange(0.5, 2, 0.5))
'''

def main():
    pass



if __name__ == "__main__":
    main()
