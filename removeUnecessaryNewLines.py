data_path = "ultraFinale.txt"
num = -1
unfinished = False
first = True
f = open(data_path, encoding="utf8")
lastLine = ""
lines = f.readlines()
for line in lines:
    num += 1
    if len(line) <= 1 and line != "\n":
        lines.pop(num)
num = -1
for line in lines:
    num += 1
    if line == "\n" and line == lastLine:
        lines.pop(num)
    lastLine = line
f.close()

new_file = open("lastFinal.txt", 'w', encoding="utf-8")

for line in lines:
    new_file.write(line)

new_file.close()
