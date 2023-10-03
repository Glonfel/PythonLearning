import random

numero_alvo = random.randint(0,100)
tentativas = 0

while True:
    num = int(input("Adivinhe o número! (0 a 100): \n"))
    tentativas += 1

    if num < numero_alvo:
        print("Menor! seu número é menor que o número sortido")
    elif num > numero_alvo:
        print("Maior! seu número é maior que o número sortido")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break