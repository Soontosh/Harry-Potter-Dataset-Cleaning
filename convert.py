f = open("singleLine.txt", encoding="utf-8")
lines = f.readlines()

mystr = ''.join([line.strip() for line in lines])
f.close()

print(mystr)

new_file = open("finalPotter.txt", 'w', encoding="utf-8")

new_file.write(mystr)

new_file.close()