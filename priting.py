import numpy as np
import matplotlib.pyplot as plt
import re
from word import word_analyze

class printing():

    def __init__(self):
        self.ax = plt.gca()
        self.ax.spines['top'].set_color('black')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.xaxis.set_ticks_position('top')   
        self.ax.yaxis.set_ticks_position('left')
        self.ax.invert_yaxis()
        self.count = 0
        self.for_ = []
        self.orgin=[]
        self.scale=[]
        self.rot=[]
        self.x_p=[]
        self.y_p = []
    
    def get_data(self,sentence):

        for sent in sentence:
            if re.search("FOR T FROM [a-zA-Z0-9*/(),]+ TO [a-zA-Z0-9*/(),]+ STEP [a-zA-Z0-9*/(),+-]+ DRAW [a-zA-Z0-9*/(),+-]+",sent,re.I):
                m = re.search("FOR T FROM ([a-zA-Z0-9*/(),]+) TO ([a-zA-Z0-9*/(),]+) STEP ([a-zA-Z0-9*/(),+-]+) DRAW \(([a-zA-Z0-9*/(),+-]+)\)",sent,re.I)
                self.for_.append((m.group(1),m.group(2),m.group(3),m.group(4).split(",")[0],m.group(4).split(",")[1]))
            if re.search("SCALE IS \(([a-zA-Z0-9*/(),]+)\)",sent,re.I):
                m = re.search("SCALE IS \(([a-zA-Z0-9*/(),]+)\)",sent,re.I)
                self.scale.append((m.group(1).split(",")[0],m.group(1).split(",")[1]))
            if re.search("ORIGIN IS \(([a-zA-Z0-9*/(),]+)\)",sent,re.I):
                m = re.search("ORIGIN IS \(([a-zA-Z0-9*/(),]+)\)",sent,re.I)
                self.orgin.append((m.group(1).split(",")[0],m.group(1).split(",")[1]))
            if re.search("ROT IS ([a-zA-Z0-9*/(),]+)",sent,re.I):
                m = re.search("ROT IS ([a-zA-Z0-9*/(),]+)",sent,re.I)
                self.rot.append(m.group(1))

    def print_(self):
        for item in range(len(self.for_)):
            start = int(self.for_[item][0])
            if re.match("pi([*/])([0-9]+)",self.for_[item][1],re.I):
                m = re.match("pi([*/])([0-9]+)",self.for_[item][1],re.I)
                if m.group(1) == "*":
                    end = np.pi * int(m.group(2))
                else:
                    end = np.pi / int(group(2))
            if re.match("pi([*/])([0-9]+)",self.for_[item][2],re.I):
                m = re.match("pi([*/])([0-9]+)",self.for_[item][2],re.I)
                if m.group(1) == "*":
                    step = np.pi * int(m.group(2))
                else:
                    step = np.pi / int(m.group(2))
            x_size = int(self.scale[item][0])
            y_size = int(self.scale[item][1])
            x_origin = int(self.orgin[item][0])
            y_origin = int(self.orgin[item][1])
            rot = int(self.rot[item])
            #print(start,end,step,x_size,y_size,rot)
            t1 = np.arange(start, end, step)
            self.x_p.append(((-np.sin(np.pi * rot / 180) *(np.sin(t1) * y_size)) + (np.cos(t1) * x_size) * np.cos(np.pi * rot / 180)) + x_origin)
            self.y_p.append(((np.cos(np.pi * rot / 180) *(np.sin(t1) * y_size)) + (np.cos(t1) * x_size) * np.sin(np.pi * rot / 180))+ y_origin)
        #print(self.x_p)
        for i in range(len(self.x_p)):
            plt.plot(self.x_p[i], self.y_p[i],'b-.',linewidth=1,label = "picture1")
        plt.show()

if __name__ == "__main__":
    b =  word_analyze("123.txt")
    b.get_string()
    a = printing()
    a.get_data(b.sentence)
    #print a.for_
    #print a.scale
    #print a.orgin
    #print a.rot
    a.print_()