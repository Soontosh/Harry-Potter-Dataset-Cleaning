#gyiewf = ...
#Issue: Sometimes there is dialogue with no speaker, you don't want to append that
#THE "said Harry" isn't on the same line as the dialogue, but instead only one line after. Make them on the same line
data_path = "merge_from_ofoct.txt"
num = -1
unfinished = False
first = True
lines = []
f = open(data_path, encoding="utf8")
allLine = f.readlines()
lastLine = ""
lastLastLine = ""
lastNum = -2
for line in allLine:
    num += 1
    if line [:4] == "Page":
        allLine.pop(num)
    else:
        pass
    lastLastLine = lastLine
    lastLine = line
    lastLastNum = lastNum
    lastNum = num
lines = allLine
f.close()
print("done")

new_file = open("ayoNoPageButEllipse.txt", 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
