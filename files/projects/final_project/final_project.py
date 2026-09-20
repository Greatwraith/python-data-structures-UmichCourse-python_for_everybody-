fhand = open('files/projects/final_project/mbox-short.txt')

for allLine in fhand:
    allLine = allLine.rstrip()
    allLine = allLine.upper()
    print(allLine)