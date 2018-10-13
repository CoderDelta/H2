# -*- coding: utf-8 -*-

#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Lab  H2                       -#
#-                                                  -#
#----------------------------------------------------#

from PIL import Image
import scipy.misc as misc
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
    img = misc.imread(sy, mode='L')
    mid_line = img[len(img)//2]
    plt.plot([wavelength[index]]*2,[0,max(mid_line)], color ='grey')
    print(max(mid_line))

    
    
index = 0     
for i in range(1,70):
    sy ='('+ str(i)+')'  + '.jpg'
    print(sy)
    spectr(sy,index,wavelength)
    index += 1
plt.yticks([0,350])
plt.plot([656.3]*2,[0,350], color =((239/255,0,0,255/255)))
plt.plot([485.1]*2,[0,350], color =((0,238/255,255/255,255/255)))
plt.plot([434.1]*2,[0,350], color =((37/255,0,240/250,255/255)))
plt.plot([410.2]*2,[0,350], color =((103/255,0,181/255,255/255)))
plt.savefig('/home/bohdan/lab_Atomca/H2/Igor_lb/image/intence.png')
plt.show()
