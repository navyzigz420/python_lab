import sys


pippo = [("Luca", 49),("Don", 72),("Leonardo da Vinci Vincioni", 13),("Tatiana",48)]


def PrintSymbol(listy):
    for x in listy:
        inclined = 20 - len(x[0])
        if len(x[0]) >= 20:
            sys.stdout.write(x[0][0:19] + ":" + " ")
            sys.stdout.write('*' * x[1]+"\n")

        else:

            sys.stdout.write(x[0]+":"+ ' ' * inclined) 
            sys.stdout.write('*' * x[1]+"\n")
        #sys.stdout.write("\n")
        #print()

def PrintWord(listy2):
    print('listy2[0]: PrintSymbol')

#PrintWord(list1)
PrintSymbol(pippo)

