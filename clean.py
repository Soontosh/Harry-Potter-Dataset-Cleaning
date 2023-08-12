import re
data_path = "cleanedPotter.txt"
cleaned = "trueNoPage.txt"
num = -1
unfinished = False
first = True
lines = []
f = open(data_path, encoding="utf8")
for line in f:
    lines.append(line)
f.close()
#print(lines)
#print("Start: Gamers")
for line in lines:
    #print(line)
    page = ""
    num += 1
    stops = 0
    addNum = 0
    currList = -1
    locNum = -1
    word = ""
    finalSent = ""
    if "Page" in line or "J.K." in line:
        lines.pop(num)

    

new_file = open(cleaned, 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
