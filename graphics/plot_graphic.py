# Imports:
import numpy as np
import matplotlib.pyplot as plt

def plot_graphic(top5, top10, topic):
    # Defines the Metrics names and colors:
    METRICS = ['CV', 'CP', 'CUCI', 'CUMASS', 'CNPMI', 'CA']
    COLORS = ['#FF7F00', '#0000FF', '#00FF00', '#FF0000', '#8B00FF', '#E0C800']
    # Creates the figure that will be ploted:
    figure = plt.figure(figsize=(15, 8))
    ## Figure 1 will plot the top-5 metrics scores:
    plot1 = figure.add_subplot(121)
    plot1.set_title(str(topic) + ' TOP-5 Metrics Scores')
    plot1.grid(linestyle='-', color='#eeeeee')
    plot1.set_ylabel("Metric Score")
    plot1.set_xlabel("Number of Intrusive Words")
    plt.xticks(range(0, 3), ['Original Topic', '1', '2'])
    plt.yticks(np.arange(-5,5, 0.1))
    for metric in range(0,6):
        if metric == 3:
            plot1.plot(range(0,3), abs(top5[:,[metric]]), 'o-', color=COLORS[metric], linewidth = 1, label=METRICS[metric]+' Coherence')
        else:
            plot1.plot(range(0,3), top5[:,[metric]], 'o-', color=COLORS[metric], linewidth = 1, label=METRICS[metric]+' Coherence')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=3, mode="expand", borderaxespad=0.)
    ## Figure 2 will plot the top-10 metrics scores:
    plot2 = figure.add_subplot(122)
    plot2.set_title(str(topic) + ' TOP-10 Metrics Scores')
    plot2.grid(linestyle='-', color='#eeeeee')
    plot2.set_ylabel("Metric Score")
    plot2.set_xlabel("Number of Intrusive Words")
    plt.xticks(range(0, 5), ['Original Topic', '1', '2', '3', '4'])
    plt.yticks(np.arange(-5,5, 0.1))
    for metric in range(0,6):
        if metric == 3:
            plot2.plot(range(0,5), abs(top10[:,[metric]]), 'o-', color=COLORS[metric], linewidth = 1, label=METRICS[metric]+' Coherence')
        else:
            plot2.plot(range(0,5), top10[:,[metric]], 'o-', color=COLORS[metric], linewidth = 1, label=METRICS[metric]+' Coherence')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=3, mode="expand", borderaxespad=0.)
    # Saves the graphics from Figure 1 into the plots folder:
    figure.savefig('plots/graph_' + str(topic) + '.png', bbox_inches='tight')
    return True
