input_file = open('scores.csv', 'r')
scores = input_file.read().split('\n')
output_file = open('scores_clean.txt', 'w')

for topic in scores:
    topic = topic.replace(",", ":")
    topic = topic.replace("[", "")
    topic = topic.replace("]", "")
    topic = topic.replace("'", "")
    topic = topic.replace(".", ",")
    output_file.write(topic + "\n")
