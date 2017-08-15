## Instructions
Before doing anything, you need to download and unzip the word embeddings. This can be done with:

```
wget http://nlp.stanford.edu/data/glove.6B.zip
```
Next run:
```
python -i findSimilarity.py
```
In the interactive python console, you can type 
```
searchBooks([word])
```
To get books whose vectors best match the word embedding for the word you entered. 
```
Do not edit the titles.dat
