import json
import random

myprefix=[]
myprefixmeaning=[]
myrootwords=[]
myrootmeaning=[]
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

# for r in range(0,len(roots['rootwords']),1):
#     print(roots['rootwords'][r].get('word'))
#     for m in range(0,len(roots['rootwords'][r]['meaning']),1):
#         print(roots['rootwords'][r]['meaning'][m])
#     print()    


def get_random_word():
    r = random.randint(0, len(roots['rootwords']))
    myrootwords = roots['rootwords'][r]['word']
    d = random.randint(0, len(roots['rootwords'][r]['meaning']))
    print(str(r)+" "+str(d))
    if d < 2:
        d = 0
    print(str(r) + " " + str(d))
    myrootwords = roots['rootwords'][r]['word']
    print(myrootwords)
    rootmeaning = roots['rootwords'][r]['meaning'][d-1]
    print(myrootwords + " " + rootmeaning)

while(True):
    get_random_word()

# for i in range(0,len(pre['prefixes']),1):
#     myprefix.append(pre['prefixes'][i]['prefix'])
#     myprefixmeaning.append(pre['prefixes'][i]['meaning'])

# for i in range(0,len(rot['roots']),1):
#     myrootwords.append(rot['roots'][i]['root'])
#     myrootmeaning.append(rot['roots'][i]['meaning'])


# for i in range(0,len(suf['suffixes']),1):
#     mysuffix.append(suf['suffixes'][i]['suffix'])
#     mysuffixmeaning.append(suf['suffixes'][i]['meaning'])


# def showwords(words):
#     for w in words:
#         print(w)


# def get_random_word():
#     randint = random.randint(0,len(myrootwords))
#     myquestion.append(rot['roots'][randint]['root'])
#     myquestion.append(rot['roots'][randint]['meaning'])


# def show_question():
#     ans=""
#     while ans != 'quit':
#         ans = input("what is the meaning of: " + myquestion[0]+"\n")
#         if ans == myquestion[1]:
#             myquestion.clear()
#             print("You are correct!")
#             num_correct =+ 1
#             get_random_word()
#         elif ans == quit:
#             return
#         else:
#             print("You are wrong...")
#             print(myquestion[1])
#             myquestion.clear()
#             get_random_word()

# get_random_word()
# show_question()