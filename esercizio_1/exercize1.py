mylist = [8, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

mylist2 = [3, 3, 3, 9, "pippo", [1,2,3]]

#soglia = 5


#print(Finale)

def listastrana(anylist, soglia):
    finale = []
    for elemento in anylist:
        try:
            if elemento >= soglia:
                finale.append(elemento)
        except TypeError:
            print("Porca vacca! Mi hai dato una lista sporca. Cosa e’  "
                  +str(type(elemento)) +"?")
    return finale
            
# Implementazione alternative usando le list comprehension
#def listastrana2(anylist, soglia):
#    return [elemento for elemento in anylist if elemento >= soglia]

print(listastrana(mylist, 2))
print(listastrana(mylist2, 2))

    