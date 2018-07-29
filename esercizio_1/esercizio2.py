def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("Non ci sono dei numeri communi") 
          
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_member(a, b)






import random
lista = []
for x in range(random.randint(1,101)):
  lista.append(random.randint(1,101))
  print(lista)
