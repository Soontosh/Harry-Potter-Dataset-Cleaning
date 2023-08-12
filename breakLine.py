#2,400,000
#@ = " and ~ = "
gg = 20
gyiewf = ...
from mmap import PAGESIZE
import sys
import codecs
data_path = "bSingleLine.txt"
num = -1
nextNum = num + 1
unfinished = False
first = True
f = open(data_path, encoding="utf-8")
lineInput = f.readlines()
lastLine = ""
lastLastLine = ""
lastNum = -2
quote = False
first = True
lastLetter = "T"
newLetter = True
ellipse = False
##print(allLine.decode('utf-8').encode('cp850','replace').decode('cp850'))
lineList = []
lines = []

allLine = []
buh = "".join(lineInput)
yuh = buh.encode("utf-8")
for i in yuh.decode("utf-8"):
    bruh = i.encode("utf-8")
    
    allLine.append(bruh)

line = []
ellipse = True
#print(len(allLine))
for trapKing in allLine:
    letter = codecs.decode(trapKing)
    gg += 1
    if gg < 3:
        pass
    else:
        ellipse = False
    if num % 100000 == 0:
        print(num)
    if not newLetter:
        num += 1
        if letter == "~":
            ##print("i")
            quote = True
        elif letter == "@":
            ##print("nah")
            quote = False
        elif letter == "." and not quote:
            line.append(letter)
            if ellipse == True:
                line.append("@")
                ellipse = False
            try:
                if allLine[nextNum+1] == "." and not allLine[nextNum+3] == ".":
                    print("yuh")
                    pass
                elif allLine[nextNum+1] == "." and allLine[nextNum+3] == ".":
                    line.insert(0, "~")
                    ellipse = True
                    gg = 0
                else:
                    stringLine = "".join(line)
                    #print(stringLine)
                    lines.append(stringLine[2:])
                    lines.append("\n")
                    newLetter = True
                    line = []
                    num += 1
                    nextNum = num + 1
                    lastNum = num
                    lastLetter = letter
            except:
                stringLine = "".join(line)
                #print(stringLine)
                lines.append(stringLine)
                lines.append("\n")
                newLetter = True
                line = []
                num += 1
                nextNum = num + 1
                lastNum = num
                lastLetter = letter

                continue
        else:
            pass
        line.append(letter)
        nextNum = num + 1
        lastNum = num
        lastLetter = letter
    else:
        num += 1
        newLetter = False
        line.append(letter)
        if letter == "~":
            #print("yuh")
            quote = False
        elif letter == "@":
            quote = True
        nextNum = num + 1
        lastNum = num
        lastLetter = letter
        
    
    nextNum = num + 1
    lastNum = num

f.close()
g = 0
for i in lines:
    g += 1
    if g <= 100:
        print(i)
trueFile = []
for i in lines:
    if len(i) <= 10 and i != "\n":
        print(i)
    else:
        trueFile.append(i)
new_file = open("endLineCheckpointTest.txt", 'w', encoding="utf-8")

for line in trueFile:
    new_file.write(line)

new_file.close()
