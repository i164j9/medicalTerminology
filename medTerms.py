import json
import random

myprefix=[]
myprefixmeaning=[]
word=[]
mymeaning=[]
mysuffix=[]
mysuffixmeaning=[]
myquestion=[]

num_correct = 0
num_wrong = 0

pre =""
roots=""
suf=""

with open("C:\\Users\\dev\\Documents\\medicalTerminology\\prefix.json",'r') as prefix:
    pre = json.load(prefix)

with open("C:\\Users\\dev\\Documents\\medicalTerminology\\root.json",'r') as root:
    roots = json.load(root)

with open("C:\\Users\\dev\\Documents\\medicalTerminology\\suffix.json",'r') as suffix:
    suf = json.load(suffix)

prefix.close()
root.close()
suffix.close()

while(True):
    n = random.randint(0,len(roots['rootwords']))
    o = random.randint(0,len(roots['rootwords'][n]['meaning']))
    print(n)
    print(o)
    defin=''
    word=''
    try:
        defin = roots['rootwords'][n]['meaning'][o]
    except (IndexError) as e:
            if e == "IndexError: list index out of range":
                defin = roots['rootwords'][n]['meaning'][o-1]
                pass
    try:
        word = roots['rootwords'][n]
    except (IndexError) as e:
            word = roots['rootwords'][n-1]
    print(word)
    print(defin)
    if n == 0:
        print(len(roots['rootwords']))
        break
    elif n == 407:
        print(len(roots['rootwords']))
        break
    