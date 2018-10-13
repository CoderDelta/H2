# -*- coding: utf-8 -*-

#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Lab  H2                       -#
#-                                                  -#
#----------------------------------------------------#

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams



rcParams["font.size"] = "22"
fig1 = plt.figure(facecolor='white', figsize=(18, 4))
ax1 = plt.axes(frameon=True)
ax1.set_facecolor('black')
ax1.get_xaxis().tick_bottom()
ax1.tick_params(colors='black')
ax1.yaxis.set_visible(False)
plt.ylabel("...", labelpad=15)

plt.plot([669.1]*2,[0,10], color ='black')
plt.plot([656.3]*2,[0,10], color =((239/255,0,0,255/255)))
plt.plot([486.1]*2,[0,10], color =((0,238/255,255/255,255/255)))
plt.plot([434.1]*2,[0,10], color =((37/255,0,240/250,255/255)))
plt.plot([410.2]*2,[0,10], color =((103/255,0,181/255,255/255)))
plt.plot([404.2]*2,[0,10], color ='black')

plt.savefig('/home/bohdan/lab_Atomca/H2/Igor_lb/image/H2.png')
        

404
plt.show()
