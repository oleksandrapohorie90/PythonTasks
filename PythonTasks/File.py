import heapq
from collections import Counter

min_heap = list()

word = "banana"

heapq.heapify(min_heap)

for letter,freq in Counter(word).items():
    heapq.heappush(min_heap,(-freq,letter))

matching = dict()
idx = 1
while min_heap:
        freq,letter = heapq.heappop(min_heap)
        matching[letter]=idx
        idx+=1
print(matching)

encoded = list()

for letter in word:
    encoded.append(matching[letter])

print(encoded)