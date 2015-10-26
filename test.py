# Disconnect from Skynet
# Skobatorium TestMania 0.2a

import time
import random


def fakeLoader():
    # Useless Loading "Animation" :)
    countingNumber = 0
    linebreaks = "\n" * 100
    print(linebreaks)
    for i in range(1,100):
        if countingNumber < 100:
            print("TestMania 0.2a" + "\n")
            countingNumber = countingNumber + random.randrange(20,random.randrange(30,50))
            if countingNumber < 100:
                print("Loading: " + str(countingNumber) + "%")
                time.sleep(random.randrange(1,2))
                print(linebreaks)
            elif countingNumber >= 100:
                 print("Loading: 100 %")
                 print("Loading: Done!" + "\n" * 3)


def split_sentence(inputText):
    # Split the inputText into a string-list and return it
    splitted_sentence = inputText.split()
    return splitted_sentence


def scramble_word(splitted_sentence):
    # Shuffle every single word,
    # keep first and last char and return the sentence
    final_sentence = []
    for i in splitted_sentence:
        middleLetterList = []
        buildWord = []
        finalWord = []
        for (j, letter) in enumerate(i):
            wordLetterCount = len(i) - 1
            if j == 0:
                firstChar = letter
                buildWord.append(firstChar)
            elif j > 0 and j < wordLetterCount:
                middleLetterList.append(letter)
                if len(middleLetterList) == wordLetterCount - 1:
                    random.shuffle(middleLetterList)
                    buildWord.append(''.join(middleLetterList))
            elif j == wordLetterCount:
                lastChar = letter
                buildWord.append(lastChar)
                for k in buildWord:
                    finalWord.append(''.join(k))
                final_sentence.append(''.join(finalWord))
    return final_sentence


if __name__ == "__main__":
    fakeLoader()
    inputText = input("Enter Text: ")
    splitted_sentence = split_sentence(inputText)
    scrambled_sentence = scramble_word(splitted_sentence)
    print("\n" + "Output Text: " + ' '.join(scrambled_sentence))
