import json
from jsonpath_ng import jsonpath

from io import StringIO
mydict={}
prefix = open("C:\\Users\\dev\\Documents\\medicalTerminology\\prefix.json",'r')
root = open("C:\\Users\\dev\\Documents\\medicalTerminology\\roots.json",'r')
suffix = open("C:\\Users\\dev\\Documents\\medicalTerminology\\suffix.json",'r')

pre = json.load(prefix)
rot = json.load(root)
suf = json.load(suffix)

print(len(rot))
for i in rot['roots']:
    mydict..append(i)
    print(i)

root.close()

for i in mylist:
    entry = mylist
    print(entry)
    


# from io import StringIO

# io = StringIO('["streaming API"]')

# print(json.load(io))
