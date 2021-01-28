n = int(input("Digite o valor de n (n > 0): "))

if n == 2 or (n != 1 and n % 2 == 1): 
        é_primo = True
else:
        é_primo = False  
divisão = 3
while divisão < n // 2 and é_primo: 
        if n % divisão == 0:
            é_primo = False
        divisão += 2
if é_primo: 
        print(n, "é primo");
else:
        print(n, "não é primo");
        
