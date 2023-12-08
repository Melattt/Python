import matplotlib.pyplot as plt
import os 
import word_set as ws
import table as tbl
import divide_text_into_words_new as dvi
import time


text = "eng_news_100K-sentences.txt"
words = dvi.read_words(text)
words = set(words)
print(len(words))

# Store sizes with associated times of execution in a dictionary (to simplify plotting on a graph)
sizes = []
times = []

# Store sizes with associated max bucket sizes
max_bucket_sizes = []

# Start with a set of length 100 and double in size every time
length = 100
while length < 200000:

    # Create a new empty set for each round
    word_set = ws.new_sized_set(length)

    # Capture start time for adding 1000 unique words from text to a "length-sized" set
    start_time = time.time()
    i = 0
    for word in words:
        i += 1
        ws.add(word_set, word)
        if i > 1000:
            break

    # Capture the time adding is done and calculate final time
    end_time = time.time()
    final_time = end_time - start_time

    # Store sizes and times in appropriate lists
    sizes.append(length)
    times.append(final_time)
    max_bucket_sizes.append(ws.max_bucket_size(word_set))

    # Values will be (10, 20, 40, 80, 160, 320, 640, 1280, ... < 20,000)
    length *= 2

plt.plot(sizes, times)
plt.show()

plt.plot(sizes, max_bucket_sizes)
plt.show()
