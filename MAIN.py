import sys


max_wordlength = 15

d = {}
#used to reduce use of .split




print("\nWord Frequency Table Generator\n\nEnter name of file to process:\n")
print("--\n")
fileToRead = input()

try:
    words = open(fileToRead,"r")
except IOError as err:
    errno, strerror = err.args
    print("I/O error({0}): {1}".format(errno, strerror))
    sys.exit()
    #detects open error and outputs error code and message
except FileNotFoundError as err:
    errno, strerror = err.args
    print("FileNotFoundError error({0}): {1}".format(errno, strerror))
    sys.exit()
    #detects open error and outputs error code and message
except NameError as err:
    errno, strerror = err.args
    print("NameError error({0}): {1}".format(errno, strerror))
    sys.exit()
    #detects open error and outputs error code and message


delimiters = [' ', ',', '.', '?', '!', ':']
# \n not needed unless you have multiples in each line

for delimiter in delimiters:
#for each delimiter, do the following
    newWords = []
    for word in words:
    #for each line in the read file
        word = word.rstrip('\n')
        #needed every time instead of in delimiter since every time you grab a new line you get a \n added at the end
        newWords += word.split(delimiter)
        #adds words separated by current delimiter from current line
    words = newWords
    #places new data into words to be processed by further delimiter checks.  [reassignment seems to render .close() unneccessary]



wordList = {}
#wordCount = []

for word in words:
    if (len(word)>max_wordlength):
        word = word[0:max_wordlength]       #restricts size of words to stated maximum

    searchingForWord = True
    while searchingForWord:
        #listPlace = 0
        for wordExists in wordList:
            if (word == wordExists):
                wordList[word] += 1
                #listPlace += 1
                searchingForWord = False
        #if not (wordList[word]):                #problem around here.  FIX IT!!!
        if (searchingForWord == True):
            wordList[word] = 1
            searchingForWord = False







print("\n--\n")
print("file processing complete.\n")
print("Word Frequency Table")
print('{:-<30}'.format(''))




#listPlace = 0
for word in wordList:
    #listPlace += 1
    print('{:<20}'.format(word), '{:<10}'.format(wordList[word]))



print("\nHISTOGRAM\n")

for word in wordList:
    print('{:<20}'.format(word),'|', end = '')

    if (wordList[word] > 10):
        print('{:X<10}'.format(''),'(',wordList[word]-10,')')
    else:
        print('{:<10}'.format('X'*wordList[word])) 



















