import random

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()

words = words.split()


# TODO: analyze which words can follow other words
start_words = []
stop_words = []
follows = {}
for i in range(len(words)-1):
    if words[i][0] == '"' and words[i][1].isupper():
        start_words.append(words[i])
    if words[i][0].isupper():
        start_words.append(words[i])
    if words[i][-1] in ['.', '?', '!']:
        stop_words.append(words[i])
    if words[i][-1] == '"' and words[i][-2] in ['.', '?', '!']:
        stop_words.append(words[i])
    if words[i] in follows:
        follows[words[i]].append(words[i+1])
    else:
        follows[words[i]] = [words[i+1]]


# TODO: construct 5 random sentences
import random
for _ in range(5):
    word = random.choice(start_words)
    while word not in stop_words:
        print(word, end=" ")
        word = random.choice(follows[word])
    print(word, '\n')


