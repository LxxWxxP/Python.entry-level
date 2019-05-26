
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for x in d.itervalues():
    sum += x
    
print sum / len(d.values())