
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

validCount = 0

for i in range(len(inputLines)):
    strArray = inputLines[i].split(" ")
    
    rangeSet = strArray[0].split('-')

    firstPosition = int(rangeSet[0])
    secondPosition = int(rangeSet[1])
    letter = strArray[1][0]
    passwordStr = strArray[2].strip()

    validPositions = 0

    wordCount = passwordStr.count(letter);

    if(passwordStr[firstPosition-1] == letter ):
        validPositions = validPositions + 1

    if(passwordStr[secondPosition-1] == letter):
        validPositions = validPositions + 1
    
    if(validPositions == 1):
        validCount = validCount + 1

print(validCount)