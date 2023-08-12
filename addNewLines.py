data_path = "lastButPeriods"
num = -1
unfinished = False
first = True
lines = []
f = open(data_path, encoding="utf8")
allLine = f.readlines()
lastLine = ""
for line in allLine:
    num += 1
    print("num")
    if line != lastLine:
        if line != "\n" and lastLine != "\n":
            allLine.insert(num, "\n")
    else:
        pass
    lastLine = line
lines = allLine
f.close()
print("done")

new_file = open("megaFinaleElNewLine.txt", 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
