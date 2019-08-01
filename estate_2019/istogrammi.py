import sys


pippo = [("Luca", 49),("Don", 22),("Leonardo da Vinci", 13),("Tatiana",48)]

pippo2 = [("Luca", 49),("Don", 72),("Leonardo da Vinci", 13),
         ("Tatiana",48), ("Matusalemme", 1200)]


def PrintSymbol(listy):

    ourMax = max([t[1] for t in listy])

    ourLimit = 50

    if ourMax <= ourLimit:
        for t in listy:
            inclined = 20 - len(t[0])
            sys.stdout.write(t[0]+ ' ' * inclined +"("+str(t[1])+"): ")
            sys.stdout.write('*' * t[1] +"\n")
    else: 
        
        for t in listy:
            inclined = 20 - len(t[0])
            sys.stdout.write(t[0]+ ' ' * inclined +"("+str(t[1])+"): ")
            newSize = round((t[1] * ourLimit) / ourMax)
            sys.stdout.write('*' * newSize + "\n")

PrintSymbol(pippo)
print("+  ==============================   +")
PrintSymbol(pippo2)

