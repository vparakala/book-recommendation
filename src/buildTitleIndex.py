def buildTitleDict():
    with open('files', 'r') as files:
        index = list()
        for book_s in files:
            try:
                book = open(book_s.rstrip(), 'r')
            except: 
                print('Could not open %s' % (book_s))
                continue
            count = 0
            for line in book:
                if 'Title: ' in line:
                    title = line.split(': ')
                    index.append((book_s.rstrip(), title[1].rstrip()))
                    break
                count+=1
                if count > 30:
                    break
    return index
def writeToOutput(index):
    outFile = open('index.dat', 'w')
    for book, title in index:
        outFile.write('%s\t%s\n' % (book, title))
index = buildTitleDict()
writeToOutput(index)
        

