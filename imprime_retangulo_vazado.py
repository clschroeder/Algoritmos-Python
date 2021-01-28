coluna = int(input("Digite a largura: "))
linha = int(input("Digite a altura: "))
i = 0
while (i < linha):
    j = 0
    while (j < coluna):
        if(i == 0 or i == linha -1 or j == 0 or j == coluna -1):
            print('#', end= '')
        else:
            print('', end = ' ')
        j = j + 1
    i = i + 1
    print()
    
