data_path = "noQuote.txt"
num = -1
unfinished = False
first = True
lines = []
f = open(data_path, encoding="utf8")
allLine = f.readlines()
for line in allLine:
    inside = False
    if line[0] == '”':
        newLine = line[2:]
        lines.append(newLine)
        #print(newLine)
    elif line[0] == "“":
        if "”" in line:
            inside = True
        if not inside:
            newLine = line[:-1]
            newLine += "”jah"
            lines.append(newLine)
            print(newLine)
        else:
            pass
    else:
        lines.append(line)
f.close()

new_file = open("ultraFinale.txt", 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
