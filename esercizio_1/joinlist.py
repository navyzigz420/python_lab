import random, sys


def common_member_set(lista1, lista2):
    a_set = set(lista1)
    b_set = set(lista2)
    if (a_set & b_set):
        return sorted(list(a_set & b_set))
    else:
        return []
      
def remove_list_duplicates(lista):
    cleanlist = []
    [cleanlist.append(x) for x in lista if x not in cleanlist]
    return cleanlist

def common_member(lista1, lista2):
    supportList1 = []
    for el in lista1:
        if el in lista2:
            supportList1.append(el)
            
    supportList1 = remove_list_duplicates(supportList1)
    supportList1.sort()
            
    return supportList1

def random_list():
    lista = []
    for x in range(random.randint(1,30)):
        lista.append(random.randint(1,101))
    return lista
    
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1]
#b = [1, 2, 3,  89, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

a = ["leo", "luca", "pippo", "tania", "topolino"]
b = ["giorgio", "piero", "tania", "leo", "asymov", "pino", "umberto"]

#for i in range(10000):    
#    a = random_list()
#    b = random_list()
#    if common_member(a,b) != common_member_set(a,b):
#        print(common_member(a,b))
#        print(common_member+set(a,b))
#    else:
#        sys.stdout.write(".")

print(a)
print(b)
print(common_member(a,b))
print(common_member_set(a,b))






#lista = []
#for x in range(random.randint(1,101)):
#  lista.append(random.randint(1,101))
  
 
