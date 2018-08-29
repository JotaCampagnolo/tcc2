from operator import itemgetter
from collections import OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import operator

IN_FILE = open('in.txt','r+')
text = IN_FILE.read().lower()
stop_words = set(stopwords.words('english'))

clean_text = text
for char in '!\"#$%&\'()*+,-./:;<=>?@[]\\_0123456789':
    clean_text = clean_text.replace(char, '')

text_tokens = word_tokenize(clean_text)

clean_tokens = []
for token in text_tokens:
    if token not in stop_words:
        clean_tokens.append(token)

word_dict = {}
for token in clean_tokens:
    if token not in word_dict:
        word_dict[token] = 1
    else:
        word_dict[token] += 1

word_dict = sorted(word_dict.items(), reverse=True, key=operator.itemgetter(1))

for word in word_dict:
    print(word)
