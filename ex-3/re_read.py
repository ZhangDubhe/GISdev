#wirtten by python 2.7
import re
print "2017 - 4 - 7 Homework 3: RE"
print "By Dubhe"
file = open("decisionTree.dot", 'rb')
for each in file:
    x = re.search("X", each)
    if(x):
        print "begin node"
        name = re.search("^\d+", each)
        label = re.search("X\[(\d+)\] <= \d+\.\d+", each)
        print "    name =",name.group()
        print "    expression =",label.group()
        print "end node\n"        

