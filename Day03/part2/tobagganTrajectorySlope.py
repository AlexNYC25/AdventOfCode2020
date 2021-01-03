inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

area = []

for line in inputLines:
    lineArr = list(line.strip())
    area.append(lineArr)

maxPos = len(area[0])
maxLines = len(area)


# new function for calculating hits
def treesInSlope(down, right): 
    startPos = 0
    startLine = 0
    hit = 0

    while startLine < maxLines:
        startLine += down
        if startLine >= maxLines :
            break
        startPos = (startPos + right) % maxPos
        if area[startLine][startPos] == '#':
            hit += 1

    return hit

print(treesInSlope(1,1) * treesInSlope(1,3) * treesInSlope(1,5) * treesInSlope(1,7) * treesInSlope(2,1))




