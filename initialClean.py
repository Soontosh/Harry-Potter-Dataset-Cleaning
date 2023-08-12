import re
data_path = "cleanedPotter.txt"
cleaned = "finalPotter.txt"
num = -1
unfinished = False
first = True
with open(data_path, encoding="utf8") as file:
  lines = file.readlines()
  for line in lines:
    num += 1
    stops = 0
    addNum = 0
    currList = -1
    locNum = -1
    word = ""
    finalSent = ""
    if line == "\n":
        del lines[num]
    
    fullSent = re.split('\s+', line)
    for i in fullSent:
        currList += 1
        if i == "Mr." or i == "Mrs." or i == "Ms.":
            if i == "Mr.":
                fullSent[currList] = "Mr"
            elif i == "Mrs.":
                fullSent[currList] = "Mrs"
            elif i == "Ms.":
                fullSent[currList] = "Ms"
    finalSent = fullSent[0]
    fullSent.pop(0)
    for i in fullSent:
        finalSent += " "
        finalSent += i
    sent = re.split('[!?.]', finalSent)
    if len(sent) <= 1:
        try:
            del lines[num]
        except:
            continue
        unfinished = True
        continue
    firstSent = sent[0]
    if unfinished and not first:
        newSent = lastSent + " "
        newSent += firstSent
        lines[num] += newSent
    else:
        lines[num] = firstSent
    sent.pop(0)
    lastSent = sent[-1]
    finalSentLet = lastSent[-1]
    if finalSentLet != "." and finalSentLet != "!" and finalSentLet != "?":
        sent.pop(-1)
        unfinished = True
    else:
        unfinished = False
    stops = len(sent)
    if stops > 0:
        for i in range(stops):
            addNum += 1
            locNum += 1
            sentence = sent[locNum]
            insNum = num + addNum
            lines.insert(insNum, sentence)
    first = False


new_file = open(cleaned, 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
