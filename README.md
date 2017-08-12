# book-recommendation
## Description
The goal of this project is to build a book recommendation engine based on the language used in the book. I have a set of 35000 books from Project Gutenberg (More info on how I got those books can be found in the **Data** section. I then sample 5000 words from each book. I get vector representations of each of the words from ```gensim```. I calculate a weighted average of the the 5000 vectors in the document using [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) weighting. I can then use this vector representation of the document to compare to other documents or words. Comparisons are made using [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) with higher values denoting greater similarity. 

## Data
The data was all from [Project Gutenberg](www.gutenberg.org). To download links to the ebooks, run:
```
wget -w 2 -m http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en
```
This gets links to zipped files of all English books in ```.txt ``` format. More information can be found [here](http://www.gutenberg.org/wiki/Gutenberg%3aInformation_About_Robot_Access_to_our_Pages) and should take around 30 minutes. 
The next step is getting the physical zip files for each book. This can be done with:
```
wget -w 2 $LINK
```
This should take around 25-30 hours. Then each file can be unzipped. Unzipping should take no more than an hour. Please pass in the ```-w``` flag with a value of at least 2 to prevent overloading of the Project Gutenberg's servers. 

