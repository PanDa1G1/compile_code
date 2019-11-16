# -*- coding: UTF-8 -*-
import re
from word import word_analyze
print_list = []

class Grammer():

    def __init__(self):

        self.print_list = []
        self.flag = 0

    def match(self,str_,num):
        if re.match("-",str_,re.I):
            str_ = str_[1:]
            self.flag = 1
        if re.search("[\+\-\*/]+",str_,re.I):
            char = re.search("[\+\-\*/]+",str_,re.I)
            self.print_list.append((char.group(),num))
            num += 1
            arr = str_.split(char.group())
            if self.flag:
                arr[0] = "0-" + arr[0]
                self.flag = 0
            self.match(arr[0],num)
            self.match(arr[1],num)
        elif re.match("[sin|cos]",str_,re.I):
            char = re.match("[a-z]+",str_,re.I)
            self.print_list.append((char.group(),num))
            num += 1
            arr = str_.split(char.group())
            self.match(arr[1].replace("(","").replace(")",""),num)
        else:
            self.print_list.append((str_,num))
    def print_tree(self):
        for items in self.print_list:
            if items[1] == 0:
                if re.match("[0-9]+",items[0]):
                    print "%s%.6f"%("=",int(items[0]))
                else:
                    print "%s%s"%("=",items[0])
            else:
                if re.match("[0-9]+",items[0]):
                    print "%s%.6f"%("========"*items[1],int(items[0]))
                else:
                    print "{}{}".format("========"*items[1],items[0])
        self.print_list = []
    
    def make_tree(self,sentence):
        for sent in sentence:
            if re.search("DRAW \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I):
                m = re.search("DRAW \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I).group(1)
                str_arr = m.split(",")
                for str_ in str_arr:
                    self.match(str_,0)
                    self.print_tree()
            elif re.search("ORIGIN IS \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I):
                m = re.search("ORIGIN IS \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I).group(1)
                str_arr = m.split(",")
                for str_ in str_arr:
                    self.match(str_,0)
                    self.print_tree()
            elif re.search("SCALE IS \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I):
                m = re.search("SCALE IS \(([a-z0-9()\-\+/\*,]+)\)",sent,re.I).group(1)
                str_arr = m.split(",")
                for str_ in str_arr:
                    self.match(str_,0)
                    self.print_tree()
            elif re.search("ROT IS ([a-z0-9()\-\+/\*,]+)",sent,re.I):
                m = re.search("ROT IS ([a-z0-9()\-\+/\*,]+)",sent,re.I).group(1)
                str_arr = m.split(",")
                for str_ in str_arr:
                    self.match(str_,0)
                    self.print_tree()


if __name__ == "__main__":
    a = word_analyze("123.txt")
    a.get_string()
    #print a.sentence
    a.analyze()
    a.print_result()
    print "[*]printing grammer tree...."
    g = Grammer()
    g.make_tree(a.sentence)


            