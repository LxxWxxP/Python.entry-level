L = range(1, 101)
print L[-10:]
print L[4::5][-10:]

L = ['Adam', 'Lisa', 'Bart', 'Paul']

L[-2:]
['Bart', 'Paul']

L[:-2]
['Adam', 'Lisa']

L[-3:-1]
['Lisa', 'Bart']

L[-4:-1:2]
['Adam', 'Bart']
