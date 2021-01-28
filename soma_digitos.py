n = int(input("Digite um número inteiro: "))

soma_n = 0

while (n > 0):

    r = n % 10
    n = n // 10
    soma_n = soma_n + r


print(soma_n)
