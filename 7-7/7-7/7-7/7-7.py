def average(*args):
    ave = 0.0
    sum = 0.0
    if len(args)==0:
        return sum
    else:
        for x in args:
            sum += x
        ave = sum / len(args)
        return ave
    
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
