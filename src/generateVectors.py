NUM_BOOKS = 36513
def genWordEmbeddingsDict():
    print('Loading Word Embeddings')
    wordEmbeddings = open('glove.6B.100d.txt', 'r')
    embeddingsDict = {line.split()[0]: map(float, line.split()[1:]) for line in wordEmbeddings}
    wordEmbeddings.close()
    print('Done')
    return embeddingsDict

def genDocEmbeddings(embeddingsDict):
    count = 0
    with open('tfidfs', 'r') as files:
        for line in files:
            count += 1
            print('Processing %d of %d' % (count, NUM_BOOKS))
            with open(line.rstrip(), 'r') as currBook:
                bookEmbedding = [float(0) for _ in range(100)]
                tfidfDict = loadDict(currBook)
                for word in tfidfDict.keys():
                    try:
                        wordEmbedding = embeddingsDict[word]
                        weight = tfidfDict[word]
                        bookEmbedding = add(bookEmbedding, wordEmbedding, weight)
                    except KeyError:
                        pass
                name = line.rstrip()[:-6]+'.vector'
                writeOutput(name, bookEmbedding)

def loadDict(inFile):
    outDict = {}
    count = 0
    for line in inFile:
        count = count + 1
        if count > 100:
            break
        data = line.split('\t')
        word = data[0].rstrip()
        weight = float(data[1])
        outDict[word] = weight
    return outDict

def add(currSum, addend, weight):
    weightedAddend = [weight * a for a in addend]
    newSum = [i + j for i, j in zip(currSum, weightedAddend)]
    return newSum

def writeOutput(name, vector):
    with open(name, 'w') as out:
        for num in vector:
            out.write('%f\n' % (num))

embeddingsDict = genWordEmbeddingsDict()
genDocEmbeddings(embeddingsDict)
                 
                

