import requests
from bs4 import BeautifulSoup
import pdfplumber

#------------------------------------------------------------------------------------------------
lista_nomes = []
#------------------------------------------------------------------------------------------------
import pdfplumber

with pdfplumber.open("Lista_Nomes_Proprios.pdf") as pdf:
    for pages in pdf.pages:
        for tabelas in pages.extract_tables():
            for linhas in tabelas:
                if("GÉNERO" not in linhas[0]):
                    lista_nomes.append(linhas[1])
                print(linhas)

print(lista_nomes)
print(len(lista_nomes))
#------------------------------------------------------------------------------------------------
for nomes in lista_nomes:
    with open("nomes.txt", "a", encoding="utf-8") as f:        
        f.write(nomes + "\n")

#------------------------------------------------------------------------------------------------