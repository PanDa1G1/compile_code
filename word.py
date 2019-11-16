import re
import collections
import math
import string
import sys

class word_analyze():

    def __init__(self,file):

        self.dict = {
            "//":"COMMENT",
            "--":"COMMENT",
            ";":"SEMICO",
            "(":"L_BRACKET",
            ")":"R_BRACKET",
            ",":"COMMA",
            "+":"PLUS",
            "-":"MINUS",
            "*":"MUL",
            "/":"DIV",
            "**":"POWER",
            "ORIGIN":"ORIGIN",
            "SCALE":"SCALE",
            "ROT":"ROT",
            "IS":"IS",
            "FOR":"FOR",
            "FROM":"FROM",
            "TO":"TO",
            "STEP":"STEP",
            "DRAW":"DRAW",
            "SIN":"FUNC",
            "COS":"FUNC",
            "TAN":"FUNC",
            "LN":"FUNC",
            "EXP":"FUNC",
            "SQRT":"FUNC",
            "T":"T"
        }
        self.file = file
        self.print_list = []
    
    def get_string(self):
        with open(self.file,"r") as f:
            tem_tring = f.read()
            self.sentence = tem_tring.split(";")
            self.sentence.pop(len(self.sentence)-1)

    def getfunctionbyname(self,module_name, function_name):
        module = __import__(module_name)
        return getattr(module, function_name)

    def analyze(self):
        for sentence in self.sentence:
            if re.match(r"[FOR|SCALE|ROT|ORIGIN]",sentence,re.I):
                if re.match(r"FOR",sentence,re.I):
                    temp_string = re.findall(r"FOR T FROM [a-zA-Z0-9*/(),]+ TO [a-zA-Z0-9*/(),]+ STEP [a-zA-Z0-9*/(),+-]+ DRAW [a-zA-Z0-9*/(),+-]+",sentence)
                elif re.match(r"SCALE",sentence,re.I):
                    temp_string = re.findall(r"SCALE IS [a-zA-Z0-9*/(),]+",sentence)
                elif re.match(r"ROT",sentence,re.I):
                    temp_string = re.findall(r"ROT IS [a-zA-Z0-9*/(),]+",sentence)
                else:
                    temp_string = re.findall(r"ORIGIN IS [a-zA-Z0-9*/(),]+",sentence)
                if temp_string:
                    for_list = temp_string[0].split(" ")
                    for str_ in for_list:
                        if str_ in self.dict.keys():
                            self.print_list.append((self.dict[str_],str_,"%.6f"%0,"NULL"))
                        elif re.match(r"[0-9]+",str_):
                            self.print_list.append(("CONST_ID",str_,"%.6f"%int(str_),"NULL"))
                        elif re.match(r"(PI)([*|/])([0-9]+)",str_,re.I):
                            m = re.match(r"(PI)([*|/])([0-9]+)",str_,re.I)
                            self.print_list.append(("CONST_ID",m.group(1),"%.6f"% math.pi,"NULL"))
                            self.print_list.append((self.dict[m.group(2)],m.group(2),"%.6f" % 0,"NULL"))
                            self.print_list.append(("CONST_ID",m.group(3),"%.6f"%int(m.group(3)),"NULL"))
                        else:
                            length = len(str_)
                            self.print_list.append((self.dict[str_[0]],str_[0],"%.6f"%0,"NULL"))
                            mid_str = str_[1:length-1]
                            if re.match("([0-9]*)(,)([0-9]*)",mid_str):
                                m_ = re.match("([0-9]*)(,)([0-9]*)",mid_str)
                                self.print_list.append(("CONST_ID",m_.group(1),"%.6f"%int(m_.group(1)),"NULL"))
                                self.print_list.append((self.dict[m_.group(2)],m_.group(2),"%.6f"%0,"NULL"))
                                self.print_list.append(("CONST_ID",m_.group(3),"%.6f"%int(m_.group(3)),"NULL"))
                            if re.match("([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([a-z]+)(\()([a-z]+)([\+\-\*/]*)([0-9]*)(\))([\+\-\*/]*)([0-9]*)(,)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([a-z]+)(\()([a-z]+)([\+\-\*/]*)([0-9]*)(\))([\+\-\*/]*)([0-9]*)",mid_str,re.I):
                                m = re.match("([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([a-z]+)(\()([a-z]+)([\+\-\*/]*)([0-9]*)(\))([\+\-\*/]*)([0-9]*)(,)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([0-9]*)([\+\-\*\/]*)([a-z]+)(\()([a-z]+)([\+\-\*/]*)([0-9]*)(\))([\+\-\*/]*)([0-9]*)",mid_str,re.I)
                                for i in m.groups():
                                    if re.match(r"[a-z]{2,}",i,re.I):
                                        self.print_list.append((self.dict[i.upper()],i.upper(),"%.6f"%0,repr(self.getfunctionbyname("math",i))))
                                    elif re.match(r"[0-9]+",i,re.I):
                                        self.print_list.append(("CONST_ID",i,"%.6f"%int(i),"NULL"))
                                    elif not i:
                                        continue
                                    else:
                                        self.print_list.append((self.dict[i.upper()],i.upper(),"%.6f"%0,"NULL"))
                            self.print_list.append((self.dict[str_[length-1]],str_[length-1],"%.6f"%0,"NULL"))
            else:
                print "[-]type error"
                sys.exit(0)

    def print_result(self):

        print "{:<{}}".format("type",16),"{:<{}}".format("lexeme",16),"{:<{}}".format("value",16),"{:<{}}".format("FuncPtr",16)
        print "="*100
        for item in self.print_list:
            print "{:<{}}".format(item[0],16),"{:<{}}".format(item[1],16),"{:<{}}".format(item[2],16),"{:<{}}".format(item[3],16)

if __name__ == "__main__":
    a = word_analyze("123.txt")
    a.get_string()
    a.analyze()
    a.print_result()