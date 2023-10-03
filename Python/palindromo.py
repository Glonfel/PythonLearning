def check_palindromo (palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

recebe_palavra = input("Insira uma palavra ou frase aqui: \n")

if check_palindromo(recebe_palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")