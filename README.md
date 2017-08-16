# find-a-book
## Introduction
Enter a topic or idea you want to read about and find-a-book will comb through a library of over 35K books to find those that best match what you're looking for. Head over to the ```tools/``` directory to get started. 
## Description
The goal of this project was to build a book search engine based on the words used in the book. I had a set of 35000 books (More info on how I got those books can be found in the ```src/``` README. I vectorized each book by first sampling the words and weighting their frequencies using [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), and then using pretrained word embeddings for each of these words. (More info can be found in ```src/```). When a user enters gives a word, the word in vectorized and then compared to all the book vectors using [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). The user will see the books with the highest similarity to the word they entered. 

