## Instructions
If you want to follow the same steps I did, first download the books. The books are from [Project Gutenberg](http://www.gutenberg.org/). You can download the data using ```download.sh```. 

Next, move all the text files into one directory, and create a list of all of them and name it ```files```. With this, you can run ```sampler.py``` to get a sample of words from each book (written to ```[name].sample```).

Then run ```tfidf.py``` on ```samples``` a list of these sample files, to get each of the sample files with tfidf weightings (written to ```[name].tfidf```)

Then run ```sorter.sh``` on these ```.tfidf``` files to sort them in order of most significant to least significant words in the document (sorts them in place)

Next download word embeddings by:
```
wget http://nlp.stanford.edu/data/glove.6B.zip
```

Then run ```generateVectors.py``` on these ```.tfidf``` files to get vector representations for each of the books. (written to ```[name].vector```) I used the 100-dimensional word embeddings for this project but you can easily change them by editing a few lines in this file. 

Using these vector files, and ```findSimilarity.py``` in the ```tools/``` folder, you should be able to generate your own book-vector matrix that can be used to in similarity comparisons with words. 

Before you pass these vector files list into ```findSimilarity.py``` you also need to build an index of titles that ```findSimilarity.py``` uses to match the document vector to the title. This can be done using ```buildTitleIndex.py```. 
