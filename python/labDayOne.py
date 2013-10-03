import math

def circ(radius):
    print 'The area of yr magnificent circle is (about): ' + str(math.pi*(float(radius)**2)) + ' units squared'

def repeat():
    answer = raw_input('Want another go? ')
    if answer == 'yes' or 'y' or 'Yes' or 'Y':
        r = raw_input('Gimme a radius, buddy... ')
        circ(r)
        repeat()
    else:
        exit
    
r = raw_input('Gimme a radius, buddy... ')

circ(r)
repeat()


    