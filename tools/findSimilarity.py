NUM_BOOKS = 36513
import numpy as np
from sys import argv
def normalize(vector):
    norm = np.linalg.norm(vector)
    return vector/norm
    
def loadWordEmbeddings():
    print('Loading Word Embeddings')
    with open('embeddings/glove.6B.100d.txt', 'r') as wordEmbeddings:
        embeddingsDict = {line.split()[0]: np.array(map(float, line.split()[1:])) for line in wordEmbeddings}
    print('Done')
    return embeddingsDict

def loadTitles():
    print('Loading Titles')
    titles = list()
    with open('titles.dat', 'r') as t:
        titles = [line.rstrip() for line in t] 
    print('Done')
    return titles 

def loadDocumentVectors():
    print('Loading Document Vectors')
    documentVectors = np.zeros((NUM_BOOKS, 100))
    count = 0
    with open('vectors') as vs:
        for line in vs:
            with open(line.rstrip()) as v:
                print('Loading book %d of %d' % (count+1, NUM_BOOKS))
                vector = np.array([float(line) for line in v])
                vector = normalize(vector)
                documentVectors[count] = vector
                count += 1
    print('Done')
    return documentVectors 

def saveDocumentVectorsFile(documentVectors):
    np.save('documentVectors.npy', documentVectors)

def loadDocumentVectorsFile():
    print('Loading Document Vectors')
    documentVectors = np.load('documentVectors.npy')
    print('Done')
    return documentVectors

def searchBooks(word):
    wordEmbedding = None 
    try:
        wordEmbedding = normalize(wordEmbeddings[word.rstrip().lower()])
    except KeyError:
        print('Looks like we don\'t have that word on file')
        return 
    similarityVector = np.matmul(documentVectors, wordEmbedding)
    bestBookIndices = np.argsort(similarityVector)[-5:]
    bestBooks = [titles[i] for i in bestBookIndices][::-1]]
    return bestBooks

wordEmbeddings = loadWordEmbeddings()
titles = loadTitles()
documentVectors = loadDocumentVectorsFile()
