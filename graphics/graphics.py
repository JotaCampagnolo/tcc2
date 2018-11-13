# Imports:
from plot_graphic import plot_graphic
import numpy as np
import matplotlib.pyplot as plt

# Topics Scores:
SCORES_FILE = open('../topic_evaluation/scores.csv', 'r') # File with topics scores.
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

Top_5_Mean = (Sports_5 + Politics_5 + Religion_5 + Music_5 + Christmas_5) / 5
Top_10_Mean = (Sports_10 + Politics_10 + Religion_10 + Music_10 + Christmas_10) / 5

plot_graphic(Sports_5, Sports_10, "Sports")
plot_graphic(Politics_5, Politics_10, "Politics")
plot_graphic(Religion_5, Religion_10, "Religion")
plot_graphic(Music_5, Music_10, "Music")
plot_graphic(Christmas_5, Christmas_10, "Christmas")
plot_graphic(Top_5_Mean, Top_10_Mean, "Mean")
