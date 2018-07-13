myChar = '*'


def myPrintAstrics(myIntVar):
    if myIntVar > 0:
        if myIntVar == 1:
            print(myChar)
        else:
            print (myChar, end='' )
            myPrintAstrics( myIntVar - 1)



myInc = int(input('Enter the number of lines to be drawn: '))

if myInc == 0:
    while myInc == 0:
        myInc = int(input('Enter a number that is 1 or greater: '))

for step in range(myInc):
    step = step + 1
    myPrintAstrics(step)


