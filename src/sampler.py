NUM_BOOKS = 36513
import random
def loadSetFromFile(name):
    stopWords = set()
    with open(name, 'r') as f:
        for line in f:
            stopWords.add(line.rstrip())
    return stopWords

def trim(word):
    if len(word) == 0:
        return
    startIndex = 0
    endIndex = len(word) - 1
    while not word[startIndex].isalpha():
        startIndex += 1
        if startIndex > endIndex:
            return 
    while not word[endIndex].isalpha():
        endIndex -= 1
        if endIndex < startIndex:
            return
    return word[startIndex:(endIndex+1)].lower()

def generateSamples(fileList, stopWords):
    processed = 0
    with open(fileList, 'r') as f:
        for line in f:
            processed += 1
            print('Processing %d of %d' % (processed, NUM_BOOKS))
            sampleDict = sample(line.rstrip(), stopWords)
            name = line[:-4]+'.sample'
            writeOutput(name, sampleDict)

def sample(name, stopWords):
    sampleDict = {}
    with open(name, 'r') as n:
        for _ in range(50):
            next(n)
        for line in n:
            for word in line.split():
                word = trim(word)
                if word and word not in stopWords and not('gutenberg' in word):
                    if random.random() < 0.2: #Adjust depending on accuracy vs speed preferences
                        try:
                            sampleDict[word] += 1
                        except KeyError:
                            sampleDict[word] = 1
    return sampleDict

def writeOutput(name, outDict):
    with open(name, 'w') as n:
        for key in outDict.keys():
            n.write('%s\t%d\n' % (key, outDict[key]))

stopWords = loadSetFromFile('stopwords.txt')
generateSamples('files', stopWords)
                        
                

