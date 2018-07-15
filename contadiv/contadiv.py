# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 07:35:35 2018

@author: admin
"""
import sys
import requests
from bs4 import BeautifulSoup

#soluzione presa da SO (StackOverflow) 
# https://stackoverflow.com/questions/36039724/suppress-warning-of-url-in-beautifulsoup
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

#url = 'http://github.com'
#url = 'http://www.passani.it'

url = sys.argv[1]
r = requests.get(url)
r_html = r.text

path_folder = 'C:\\Users\\admin\\Documents\\GitHub\python_lab\\contadiv\\files\\'

filename = "il_mio_sito.htm"

path = path_folder + filename


mio_sito_file =  open(path,'w', encoding='utf8')

mio_sito_file.write(r_html)

print("Ho generato il file "+path)
mio_sito_file.close()

# =============================================================================
# contatore = 0
# with open(path,'r') as f:
#     for line in f:
#       if "div" in line:
#           contatore = contatore + 1
#           
# print("La pagina "+url + " ha " + str(contatore) + " tag DIV")
# =============================================================================


with open(path,'r') as f:
     testo = f.read()

soup = BeautifulSoup(testo)
#print("La pagina "+url + " ha " + str(len(soup.find_all("div"))) + " tag DIV")
print(str(len(soup.find_all("div"))))

 
