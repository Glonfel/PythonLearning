def fibonacci (num):
    sequencia = [0,1]
    while len(sequencia) < num:
        prox_num = sequencia [-1] + sequencia[-2]
        sequencia.append(prox_num)
    return sequencia

num = int(input("Informe o número desejado na sequência de Fibonacci a ser gerado: \n"))
res = fibonacci(num)
print(res)