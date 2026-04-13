import unicodedata
#------------------------------------------------------------------------------------------------


def limpar_texto(palavra):
    frase_sem_acentos = unicodedata.normalize('NFD', palavra)
    return "".join(c for c in frase_sem_acentos if unicodedata.category(c) != 'Mn')
#------------------------------------------------------------------------------------------------
def carregar_lista(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]
#------------------------------------------------------------------------------------------------

def gerar_wordlist(nomes, sobrenomes, separador, output_file):
    total = 0

    with open(output_file, "w", encoding="utf-8") as f:
        for i, nome in enumerate(nomes, start=1):
            nome_limpo = limpar_texto(nome)

            for sobrenome in sobrenomes:
                sobrenome_limpo = limpar_texto(sobrenome)

                combinacao = f"{nome_limpo}{separador}{sobrenome_limpo}"
                f.write(combinacao + "\n")
                total += 1

            print(f"Nomes processados: {i} | Total gerado: {total}")

    print("\n Wordlist gerada com sucesso!")
    print(f"Total final: {total}")


if __name__ == "__main__":
    nomes = carregar_lista("nomes.txt")
    sobrenomes = carregar_lista("sobrenomes.txt")

    separador = input("Escreve o separador entre nome e sobrenome (ex: ., _, -, ou deixa vazio): ")
#------------------------------------------------------------------------------------------------

    gerar_wordlist(
        nomes,
        sobrenomes,
        separador,
        "nomes_e_sobrenomes.txt"
    )