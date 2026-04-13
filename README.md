# Portuguese Names Wordlist (Portugal)

This project consists of creating a wordlist of Portuguese names by combining real first names and surnames collected from public sources.

This wordlist can be used for:
- User enumeration
- Authorized cybersecurity testing
- OSINT (Open Source Intelligence)
- Realistic username simulation
- Other research and security-related purposes

The goal is to generate realistic combinations such as:
`joao.silva`, `maria.santos`, `pedro.oliveira`

The idea is to create a wordlist with all possible combinations between Portuguese first names and surnames.

---

# Project Scripts

The project contains three main scripts:

## script_buscar_nomes.py
Used to create a wordlist of all possible Portuguese first names.

Data is obtained from:
https://irn.justica.gov.pt/Portals/33/Regras%20Nome%20Proprio/Lista%20Nomes%20Pr%C3%B3prios.pdf

This is an official Portuguese government (IRN) document containing approved given names.

### What the script does:
- Reads the PDF file containing first names
- Extracts names from tables
- Saves the output into `nomes.txt`

---

## script_buscar_sobrenomes.py
Used to create a wordlist of all possible Portuguese surnames.

Data is obtained from:
https://nosportugueses.pt/pt/apelidos/

This website contains a large alphabetical database of surnames.

### What the script does:
- Scrapes surname data from the website
- Iterates through all alphabet letters
- Extracts available surnames
- Cleans and processes data (e.g., splits hyphenated surnames)
- Saves output into `sobrenomes.txt`

---

## juntar_nome_e_sobrenome.py
Used to generate all possible combinations between first names and surnames.

Inputs:
- `data/nomes.txt`
- `data/sobrenomes.txt`

### What the script does:
- Reads first names and surnames
- Generates all possible combinations
- Allows selection of separator (e.g. `.`, `_`, `-`, or none)
- Removes accents for username compatibility
- Saves final output into `nomes_e_sobrenomes.txt`

---

# Generated Data

Inside the `data/` folder:

- `nomes.txt`: contains approximately 7,548 first names  
- `sobrenomes.txt`: contains approximately 21,422 surnames  

The file `nomes_e_sobrenomes.txt` is not included in the repository due to GitHub file size limitations.

---

# Total Combinations

The total number of possible combinations is:

```text
7,548 × 21,422 = 161,693,256 combinations
