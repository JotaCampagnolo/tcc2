import os
from operator import itemgetter
from collections import OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import operator

PATH_IN = 'sports_in/'
PATH_OUT = 'sports_out/'
IN_FILES = []
stop_words = set(stopwords.words('english'))
STEM_FUNC = PorterStemmer()
news_dict = {}
wiki_dict = {}

for file in os.listdir(PATH_IN):
    IN_FILES.append(str(file))

for file in IN_FILES:
    IN_FILE = open(PATH_IN+file,'r+')
    text = IN_FILE.read().lower()
    clean_text = text
    for char in '-':
        clean_text = clean_text.replace(char, ' ')
    for char in '!\"#$%&\'“”—–’()*+,./:;<=>?@[]\\_0123456789':
        clean_text = clean_text.replace(char, '')
    text_tokens = word_tokenize(clean_text)
    clean_tokens = []
    for token in text_tokens:
        if token not in stop_words:
            clean_tokens.append(token)
    stem_tokens = []
    for token in clean_tokens:
        stem_tokens.append(STEM_FUNC.stem(token))

    for token in stem_tokens:
        if file.find('wiki') >= 0:
            if token not in wiki_dict:
                wiki_dict[token] = 1
            else:
                wiki_dict[token] += 1
        else:
            if token not in news_dict:
                news_dict[token] = 1
            else:
                news_dict[token] += 1

news_dict = sorted(news_dict.items(), reverse=True, key=operator.itemgetter(1))
wiki_dict = sorted(wiki_dict.items(), reverse=True, key=operator.itemgetter(1))

with open(PATH_OUT+'news_out.txt', 'w') as file:
    for word in news_dict:
        file.write(str(word)+'\n')

with open(PATH_OUT+'wiki_out.txt', 'w') as file:
    for word in wiki_dict:
        file.write(str(word)+'\n')
