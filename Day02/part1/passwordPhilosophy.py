
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

validCount = 0

for i in range(len(inputLines)):
    strArray = inputLines[i].split(" ")
    
    rangeSet = strArray[0].split('-')

    minNumber = int(rangeSet[0])
    maxNumber = int(rangeSet[1])
    letter = strArray[1][0]
    passwordStr = strArray[2].strip()

    wordCount = passwordStr.count(letter);
    
    if(wordCount >= minNumber and wordCount <= maxNumber):
        validCount = validCount + 1

print(validCount)