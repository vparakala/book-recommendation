import math
NUM_BOOKS = 36513
def fileToDict(sampleFile):
    wordDict = {}
    with open(sampleFile, 'r') as s:
        for line in s: 
            data = line.split('\t')
            word = data[0]
            frequency = int(data[1])
            wordDict[word] = frequency
    return wordDict
def normalize(wordDict):
    total = 0
    for word in wordDict.keys():
        total += wordDict[word]
    normalized = {}
    for word in wordDict.keys():
        normalized[word] = (float(wordDict[word])/float(total))
    return normalized
def getIdf():
    print('Generating Idf')
    idf = {}
    count = 0
    with open('samples', 'r') as s:
        for line in s:
            count += 1
            print('Generating idf: Reading in file %d of %d' % (count, NUM_BOOKS))
            with open(line.rstrip(), 'r') as curr:
                currWordSet = set()
                for line in curr:
                    word = line.split('\t')[0]
                    currWordSet.add(word)
                for word in currWordSet:
                    try:
                        idf[word] += 1
                    except KeyError:
                        idf[word] = 1
    for word in idf.keys():
        idf[word] = math.log(float(NUM_BOOKS)/float(idf[word]))
    return idf

def genTfidf(idf):
    with open('samples', 'r') as s:
        count = 0
        for line in s:
            tfidf = {}
            count += 1
            print('Processing file %d of %d' % (count, NUM_BOOKS))
            frequencyDict = fileToDict(line.rstrip())
            normFrequencyDict = normalize(frequencyDict)
            for word in normFrequencyDict.keys():
                wordIdf = idf[word]
                tfidf[word] = wordIdf * normFrequencyDict[word]
            name = line.rstrip()[:-7]+'.tfidf'
            writeOutput(name, tfidf)

def writeOutput(name, outDict):
    with open(name, 'w') as n:
        for elem in outDict.keys():
            n.write('%s\t%f\n' % (elem, outDict[word]))

idf = getIdf()
genTfidf(idf)


                

    
        
