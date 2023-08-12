data_path = "ultraFinale.txt"
num = -1
unfinished = False
first = True
lines = []
f = open(data_path, encoding="utf8")
allLine = f.readlines()
lastLine = ""
for line in allLine:
    num += 1
    print(num)
    if line == lastLine:
        if line == "\n" and lastLine == "\n":
            allLine.pop(num)
    else:
        pass
    lastLine = line
lines = allLine
f.close()
print("done")

new_file = open("lastButPeriods", 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
