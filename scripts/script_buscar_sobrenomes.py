import requests
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------------------------
lista_sobrenomes = []
abc = "abcdefghijklmnopqrstuwvxyz"
#------------------------------------------------------------------------------------------------

def get_sobrenomes_da_site(letra):
    response = requests.get('https://nosportugueses.pt/pt/apelidos/' + letra)
    root = BeautifulSoup(response.content, "html.parser")

    first_ul = root.find("ul", {"class": "list-column"})
    items = first_ul.find_all("li", {"class": "list-item"})
    return items
#------------------------------------------------------------------------------------------------

def tratamento_de_dados(lista):
    new_list = []

    for nome in lista:

        nome = nome.strip()

        if "-" in nome:
            partes = nome.split("-")
            for parte in partes:
                new_list.append(parte.strip())
        else:
            new_list.append(nome)

    return new_list


#------------------------------------------------------------------------------------------------
for letra in abc:
    print(letra)
    lista_nomes_site = get_sobrenomes_da_site(letra)
    for sobrenomes in lista_nomes_site:
        lista_sobrenomes.append(sobrenomes.text.strip())

print(lista_sobrenomes)
lista_sobrenomes = tratamento_de_dados(lista_sobrenomes)

for sobrenome in lista_sobrenomes:
    with open("sobrenomes.txt", "a", encoding="utf-8") as f:        
        f.write(sobrenome + "\n")


print(lista_sobrenomes)
print("Nº de sobrenomes:", len(lista_sobrenomes))
      
