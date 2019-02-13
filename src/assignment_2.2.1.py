# This first 2 lines are provided for you

English = input('Enter English score: ')
English = int(English)
Math = input('Enter Math score: ')
Math = int(Math)
if English > 80:
    English = English * 1.5
total = English + Math
average = total/2
print('Average:', average)
