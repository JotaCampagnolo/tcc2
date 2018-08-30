import os
from operator import itemgetter
from collections import OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import operator

PATH_IN = 'sports_in/' # Path to input data.
PATH_OUT = 'sports_out/' # Path where the results will be saved.
IN_FILES = [] # List of input data files.
stop_words = set(stopwords.words('english')) # Stop-words to be removed from data.
STEM_FUNC = PorterStemmer() # Stemmer function that will be used.
news_dict = {} # Dictionary with news words.
wiki_dict = {} # Dictionary with wiki words.
all_dict = {} # Dictionary with all words.

# Getting input data files names:
for file in os.listdir(PATH_IN):
    IN_FILES.append(str(file))

# For each file on input data:
for file in IN_FILES:
    IN_FILE = open(PATH_IN+file,'r+')
    text = IN_FILE.read().lower() # Set the data to lowercase.
    clean_text = text
    for char in '-': # Remove '-' from words.
        clean_text = clean_text.replace(char, ' ')
    for char in '!\"#$%&\'“”—–’()*+,./:;<=>?@[]\\_0123456789': # Remove special chars.
        clean_text = clean_text.replace(char, '')
    text_tokens = word_tokenize(clean_text) # Tokenize the data.
    clean_tokens = []
    for token in text_tokens: # Remove stop-words from data.
        if token not in stop_words:
            clean_tokens.append(token)
    stem_tokens = []
    for token in clean_tokens: # Stemmize the data.
        stem_tokens.append(STEM_FUNC.stem(token))

    for token in stem_tokens: # Grouping the words into their dictionarys:
        if file.find('wiki') >= 0: # WIKIPEDIA dict:
            if token not in wiki_dict:
                wiki_dict[token] = 1
            else:
                wiki_dict[token] += 1
        else: # NEWS dict:
            if token not in news_dict:
                news_dict[token] = 1
            else:
                news_dict[token] += 1
        # GENERAL dict:
        if token not in all_dict:
            all_dict[token] = 1
        else:
            all_dict[token] += 1

# Sort the dictionarys by value:
news_dict = sorted(news_dict.items(), reverse=True, key=operator.itemgetter(1))
wiki_dict = sorted(wiki_dict.items(), reverse=True, key=operator.itemgetter(1))
all_dict = sorted(all_dict.items(), reverse=True, key=operator.itemgetter(1))

# Saves the output files:
with open(PATH_OUT+'news_out.txt', 'w') as file:
    for word in news_dict:
        file.write(str(word)+'\n')
with open(PATH_OUT+'wiki_out.txt', 'w') as file:
    for word in wiki_dict:
        file.write(str(word)+'\n')
with open(PATH_OUT+'all_out.txt', 'w') as file:
    for word in all_dict:
        file.write(str(word)+'\n')
