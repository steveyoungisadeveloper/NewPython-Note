wordList = []

outputData = open("rules", "r")
cleanData = open("cleanRule.txt", "w")

lines = outputData.readlines()

for line in lines:
    wordList = line.split()
    confidence = float(wordList[-1])
    support = int(wordList[-2])
    if confidence>= 0.6 and support >= 2:
        cleanData.writelines(line)

outputData.close()
cleanData.close()
