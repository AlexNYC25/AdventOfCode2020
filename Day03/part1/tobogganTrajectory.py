
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

area = []

for line in inputLines:
    lineArr = list(line.strip())
    area.append(lineArr)

maxPos = len(area[0])
maxLines = len(area)

startPos = 0
startLine = 0


hit = 0

while startLine < maxLines:
    startLine += 1
    if startLine >= maxLines :
        break
    startPos = (startPos + 3) % maxPos
    if area[startLine][startPos] == '#':
        hit += 1

print(hit)

