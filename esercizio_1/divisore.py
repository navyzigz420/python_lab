def diviser(numero):
    lista = []
    a = 0
    while a < numero // 2:
        a = a + 1
        if numero % a == 0:
            lista.append(a)
            
    #let's not forget the last number: the number itself!
    lista.append(numero)
    return lista

years = [1995, 1973, 2006, 1953, 1939, 1931, 1962, 1951]
#num = int(input("Numero da dividere? ")) 

for elemento in years:     
    print(diviser(elemento))


        
        
    
   
       
       
    
                
