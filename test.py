# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import re
from word import word_analyze
from matplotlib.patches import Ellipse
'''
delta = 45.0  # degrees

angles = np.arange(0, delta*1, delta)
ells = [Ellipse((220, 350), 10, 50, a) for a in angles]

a = plt.subplot(111, aspect='equal')

for e in ells:
    e.set_clip_box(a.bbox)
    e.set_alpha(0.1)
    a.add_artist(e)

ax = plt.gca()
ax.spines['top'].set_color('black')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('top')   
ax.yaxis.set_ticks_position('left')
ax.invert_yaxis()

plt.xlim(170, 270)
plt.ylim(400, 300)

plt.show()


ax = plt.gca()
ax.spines['top'].set_color('black')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('top')   
ax.yaxis.set_ticks_position('left')
ax.invert_yaxis()
'''
t1 = np.arange(0.0, np.pi * 2, np.pi / 50)
ax = plt.gca()
#plt.xticks([])
#plt.yticks([])
ax.spines['top'].set_color('black')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('top')   
ax.yaxis.set_ticks_position('left')
ax.invert_yaxis()
x = []
y = []
y0 = np.sin(t1) * 10
x0 = np.cos(t1) * 50
#x.append(x0)
#y.append(y0)
y.append((np.cos(np.pi *45 / 180) *y0 +x0 * np.sin(np.pi*45 / 180)) + 50)
x.append((-np.sin(np.pi*45 / 180) *y0 + x0 * np.cos(np.pi*45 / 180)) + 50)
y.append(np.cos(np.pi* 90 / 180) *y0 +x0 * np.sin(np.pi* 90 / 180))
x.append(-np.sin(np.pi* 90 / 180) *y0 + x0 * np.cos(np.pi* 90 / 180))
y.append(np.cos(np.pi * 135 / 180) *y0 +  x0 * np.sin(np.pi * 135 / 180))
x.append(-np.sin(np.pi* 135 / 180) *y0 +   x0 * np.cos(np.pi * 135 / 180))


#plt.ylim(320, 120)
#plt.xlim(250,450)

for i in range(len(x)):
    plt.plot(x[i], y[i],'b-.',linewidth=1,label = "picture1")                  
#plt.grid(True)
plt.show()

'''
        self.ax.spines['top'].set_color('black')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.xaxis.set_ticks_position('top')   
        self.ax.yaxis.set_ticks_position('left')
        self.ax.invert_yaxis()
'''
