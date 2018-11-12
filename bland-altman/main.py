# Imports:
from bland_altman import bland_altman_plot
import numpy as np
import matplotlib.pyplot as plt

# Topics Scores:
SCORES_FILE = open('scores.csv', 'r') # File with topics scores.
TOPICS_SCORES = SCORES_FILE.readlines()
for i in range(len(TOPICS_SCORES)):
    TOPICS_SCORES[i] = TOPICS_SCORES[i].replace("[", "")
    TOPICS_SCORES[i] = TOPICS_SCORES[i].replace("]", "")
    TOPICS_SCORES[i] = TOPICS_SCORES[i].replace("'", "")
SCORES = np.array([line.split(',')[1:] for line in TOPICS_SCORES], dtype = float) # Each line is a topic, and each column is a metric: CV | CP | CUCI | CUMASS | CNPMI | CA.

METRICS = ['CV', 'CP', 'CUCI', 'CUMASS', 'CNPMI', 'CA']

Sports_5 = SCORES[0:3]
Sports_10 = SCORES[3:8]
Politics_5 = SCORES[8:11]
Politics_10 = SCORES[11:16]
Religion_5 = SCORES[16:19]
Religion_10 = SCORES[19:24]
Music_5 = SCORES[24:27]
Music_10 = SCORES[27:32]
Christmas_5 = SCORES[32:35]
Christmas_10 = SCORES[35:40]

for i in range(0,6):
    for k in range(0,6):
        if i != k:
            m1 = SCORES[:,[i]]
            m2 = SCORES[:,[k]]
            f, ax = plt.subplots(1, figsize =(8,5))
            my_bland_altman_plot = bland_altman_plot(m1, m2, ax = ax)
            f.savefig('plots/' + METRICS[i] + '_' + METRICS[k] + '.png')
            plt.close()
