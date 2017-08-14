import random
def openFiles():
    fileList = open('files', 'r')
    stopWords = open('stopwords.txt')
    stopBooks = open('stopbooks.txt')
    return fileList, stopWords, stopBooks
def loadStopWords(stopWords):
    stopWordsSet = set()
    for line in stopWords:
        stopWordsSet.add(line.rstrip())
    return stopWordsSet
def loadStopBooks(stopBooks):
    stopBookSet = set()
    for line in stopBooks:
        stopBookSet.add(line.rstrip())
    return stopBookSet
def trim(word):
    if len(word) < 2:
        return word.lower()
    word = word.rstrip()
    charsToTrim = set(['.', ',', '!', '?', '\"', '\'', '-', ':', ';', '$', '%', '_', '\n', '\t', '(', ')'])
    if word[0] in charsToTrim:
        word = word[1:]
    if word[-1] in charsToTrim:
        word = word[:-1]
    word = word.rstrip()
    word = word.lower()
    return word
def process(fileList, stopWordsSet, stopBookSet):
    processed = 0
    for line in fileList:
        processed += 1
        print('processing %d of 36568' % (processed)) 
        if line.rstrip() not in stopBookSet:
            try:
                sampleDict = sample(line.rstrip(), stopWordsSet)
            except:
                pass
            name = line[:-4] + 'sample'
            writeOutput(name, sampleDict)

def sample(fileName, stopWordsSet):
    book = open(fileName, 'r')
    sampleDict = dict()
    for _ in range(50):
        next(book)
    for line in book:
        for word in line.split():
            word = trim(word)
            if word not in stopWordsSet and not('gutenberg' in word):
                if random.random() < 0.2:
                    if word in sampleDict.keys():
                        sampleDict[word] = sampleDict[word] + 1
                    else:
                        sampleDict[word] = 1
    return sampleDict 
def writeOutput(name, sampleDict):
    outFile = open(name, 'w')
    for key in sampleDict.keys():
        outFile.write('%s\t%d\n' % (key, sampleDict[key]))

        
fileList, stopWords, stopBooks = openFiles()
stopWordsSet = loadStopWords(stopWords)
stopBookSet = loadStopBooks(stopBooks)
process(fileList, stopWordsSet, stopBookSet)
        
    

    
    
