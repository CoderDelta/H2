# -*- coding: utf-8 -*-

#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                    Lab  H2                       -#
#-                                                  -#
#----------------------------------------------------#

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import xlrd

wavelength = np.array([[669.1],[669]])
book = xlrd.open_workbook("/home/bohdan/lab_Atomca/H2/Igor_lb/python/corect.xlsx")
first_sheet = book.sheet_by_index(0)

for n in range(2,first_sheet.nrows - 1):
    stan = first_sheet.row_values(n)
    wavelength = np.append(wavelength, [[stan[0]]],axis = 0)
rcParams["font.size"] = "22"
fig1 = plt.figure(facecolor='white', figsize=(18, 7))
ax1 = plt.axes(frameon=True)
ax1.set_facecolor('black')
ax1.get_xaxis().tick_bottom()
ax1.tick_params(colors='black')
ax1.yaxis.set_visible(False)
plt.ylabel("...", labelpad=15)

def spectr(sy,index,wavelength):
    img = Image.open(sy)
    rgba_im = img.convert('RGBA')
    width, height = img.size
    num = 0
    r = 0; g = 0; b = 0; a = 0
    for i in range(0,img.size[0]):
        for k in range(0,img.size[1]):
            n, m, k,l = rgba_im.getpixel((i, k))
            if (n+m+k) < 350 and (n+m+k) > 35:
                r += n
                g += m
                b += k
                a += l
                num +=1
    num = num * 255
    print(wavelength[index])
    for wl in wavelength[index]:
            plt.plot([wl]*2,[0,1], color =((r/num,g/num,b/num,a/num)))

        
    print(r/num,g/num,b/num,a/num)
    print('----------------------------')
    return True
    
    
index = 0     
for i in range(1,70):
    sy ='('+ str(i)+')'  + '.jpg'
    print(sy)
    spectr(sy,index,wavelength)
    index += 1

plt.savefig('/home/bohdan/lab_Atomca/H2/Igor_lb/image/spectr.png')
plt.show()
