# Disconnect from Skynet
# Skobatorium TestMania 0.1a

import time
import random

# Useless Loading "Animation"

countingNumber = 0
clearScreen = "\n" * 100

print(clearScreen)

for i in range(1,100):
    if countingNumber < 100:
        print("TestMania 0.1a" + "\n")
        countingNumber = countingNumber + random.randrange(30,random.randrange(60,90))
        if countingNumber < 100:
            print("Loading: " + str(countingNumber) + "%")
            time.sleep(random.randrange(1,2))
            print(clearScreen)
        elif countingNumber >= 100:
             print("Loading: 100 %")
             print("Loading: Done!" + "\n" * 3)
                


def scrambler():
    inputText = input("Enter Text: ")
    wordHacker = inputText.split()
    finalText = []
    for word in wordHacker:
        middleLetterList = []
        buildWord = []
        finalWord = []
        for (id, letter) in enumerate(word):
            wordMaxLengthID = len(word) - 1
            if id == 0:
                firstChar = letter
                buildWord.append(firstChar)
            elif id > 0 and id < wordMaxLengthID:
                middleLetterList.append(letter)
                if len(middleLetterList) == wordMaxLengthID - 1:
                    random.shuffle(middleLetterList)
                    buildWord.append(''.join(middleLetterList))
            elif id == wordMaxLengthID:
                lastChar = letter
                buildWord.append(lastChar)
                for flattenWord in buildWord:
                    finalWord.append(''.join(flattenWord))
                finalText.append(''.join(finalWord))
    print("\n" + "Output Text: " + ' '.join(finalText))
        
scrambler()
