import re

p1 = input('P1 enter the time to shoot: ')
p2 = input('P2 enter the time to shoot: ')
tie = 'tie'
def whos_first(p1, p2):

    counter_p1 = len(p1) - len(p1.lstrip())
    counter_p2 = len(p2) - len(p2.lstrip())


    if counter_p1 < counter_p2:
        return p1
    elif counter_p1 > counter_p2:
        p2
    else:
        return tie

whos_first(p1, p2)