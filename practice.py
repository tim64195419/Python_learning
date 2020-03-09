from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))



items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 20))))
items2 = [x ** 2 for x in range(1, 20) if x % 2]




print(items2)