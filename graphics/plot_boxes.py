# Imports:
import numpy as np
import matplotlib.pyplot as plt

# Defines the Metrics names and colors:
METRICS = ['CV', 'CP', 'CUCI', 'CUMASS', 'CNPMI', 'CA']
COLORS = ['#FF7F00', '#0000FF', '#00FF00', '#FF0000', '#8B00FF', '#E0C800']

def subplot_box(position, metric, i, figure, subplots, size):
    subplots.append(figure.add_subplot(position))
    subplots[-1].set_title(' TOP-' + str(size) + ' : ' + METRICS[i] + ' Coherence Scores', color=COLORS[i])
    subplots[-1].grid(linestyle='-', color='#eeeeee')
    subplots[-1].set_ylabel("Coherence Score")
    subplots[-1].set_xlabel("Number of Intrusive Words")
    data1 = metric[0]
    data2 = metric[1]
    data3 = metric[2]
    if len(metric) == 5:
        data4 = metric[3]
        data5 = metric[4]
    subplots[-1].boxplot(data1[:,[i]], widths=0.4, positions = [2])
    subplots[-1].boxplot(data2[:,[i]], widths=0.4, positions = [3])
    subplots[-1].boxplot(data3[:,[i]], widths=0.4, positions = [4])
    if len(metric) == 5:
        subplots[-1].boxplot(data4[:,[i]], widths=0.4, positions = [5])
        subplots[-1].boxplot(data5[:,[i]], widths=0.4, positions = [6])

    plt.plot(np.ones(5)*2, data1[:,[i]], 'o', color=COLORS[i], alpha=0.5)
    plt.plot(np.ones(5)*3, data2[:,[i]], 'o', color=COLORS[i], alpha=0.5)
    plt.plot(np.ones(5)*4, data3[:,[i]], 'o', color=COLORS[i], alpha=0.5)
    if len(metric) == 5:
        plt.plot(np.ones(5)*5, data4[:,[i]], 'o', color=COLORS[i], alpha=0.5)
        plt.plot(np.ones(5)*6, data5[:,[i]], 'o', color=COLORS[i], alpha=0.5)

    if len(metric) == 5:
        plt.xticks([1,2,3,4,5,6,7], ['','Original Topic', 1, 2, 3, 4, ''])
    else:
        plt.xticks([1,2,3,4,5], ['','Original Topic', 1, 2,''])
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    return True

def plot_boxes(TopN, size):
    # Creates the figure that will be ploted:
    figure1 = plt.figure(figsize=(20, 12))
    subplots = []
    # Creates the subplots:
    for i in range(len(METRICS)):
        subplot_box(231+i, TopN, i, figure1, subplots, size)
    # Saves the graphics from Figure 1 into the plots folder:
    figure1.savefig('plots/box_top' + str(size) + '.png', bbox_inches='tight')
    return True
