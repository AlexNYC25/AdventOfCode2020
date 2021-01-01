
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

inputNumbers = []
finalResult = 0

for line in inputLines:
    temp = int(line)
    inputNumbers.append(temp)

for i in range(len(inputNumbers)):
    for j in range(len(inputNumbers)):
        for k in range(len(inputNumbers)):
            if(j != i and i != k and k != j ):
                if(inputNumbers[i] + inputNumbers[j] + inputNumbers[k] == 2020):
                    finalResult = inputNumbers[i] * inputNumbers[j] * inputNumbers[k]
        
        
if(finalResult != 0):
    print(finalResult)