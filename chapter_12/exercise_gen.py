data1 = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [num for num in data1 if not num % 2]
print(evens)

data2 = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = [num for num in data2 if isinstance(num, str)]
print(words)

data3 = 'So long and thanks for all the fish'.split()
title = [word.title() for word in data3]
print(title)
