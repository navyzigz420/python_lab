# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 09:10:52 2018

@author: admin
"""
import sys

#path = 'C:\\Users\\admin\\Documents\\GitHub\python_lab\\contadiv\\files\\days.txt'

#print(days_file.read())
#print(days_file.readlines())

# Lettura file linea per linea
# la sintassi con 'with' e' conveniente perche' chiude il file in automatico
#with open(path,'r') as f:
#    for line in f:
#        sys.stdout.write(line) #meglio. se non vogliamo i newline \n
        

#Creiamo programmaticamente un file chiamato 'giorni.txt'

path = 'C:\\Users\\admin\\Documents\\GitHub\python_lab\\contadiv\\files\\giorni.txt'
giorni = ["lunedi'","martedi'","mercoledi'","giovedi'","venerdi'",'sabato','domenica']

giorni_file =  open(path,'w')

for elem in giorni:
    giorni_file.write(elem + "\n")

print("Ho generato il file "+path)
giorni_file.close()


    
