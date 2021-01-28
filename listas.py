n = 10
while n > 0:
    lista = [n]
    n = n + 10
    lista.append(n)
    print(lista)
    tam = len(lista) - 1
    n = int(input("Digite 0 para decrescentar a lista:"))     
    while tam >= 0:
        print(lista[tam], end=", ")
        tam = tam - 1
        





