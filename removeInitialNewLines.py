import sys
import codecs
#gyiewf = ...
#Issue: Sometimes there is dialogue with no speaker, you don't want to append that
#THE "said Harry" isn't on the same line as the dialogue, but instead only one line after. Make them on the same line
data_path = "endLineCheckpoint1.txt"
num = -1
unfinished = False
first = True
lines = []
allLine = []
poopLine = []
f = open(data_path, encoding="utf8")
bruhLine = f.readlines()
for i in bruhLine:
    crow = i.encode("utf-8")
    print("yuh:" + " " + i)
    poopLine.append(crow)

lastLine = ""
lastLastLine = ""
lastNum = -2
for bruh in allLine:
    pass
for bruh in allLine:
    nah = codecs.decode(bruh)
    line = nah
    printStuff = line.encode("utf-8")
    num += 1
    print(printStuff)
    if printStuff == "\n":
        allLine.pop(num)
        print("bruh")
lines = allLine
f.close()
print("done")

new_file = open("newLinesUltra.txt", 'w', encoding="utf-8")

for poopoo in lines:
    line = codecs.decode(poopoo)
    new_file.write(line)

new_file.close()
