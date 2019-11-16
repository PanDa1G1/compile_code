# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


class Grammer:

    def __init__(self):

        self.ax = plt.gca()
        self.ax.spines['top'].set_color('black')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.xaxis.set_ticks_position('top')   
        self.ax.yaxis.set_ticks_position('left')

            