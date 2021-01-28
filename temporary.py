a = 0
b = 0
s = 0
x = str(s)

print ('Enter the first number: ', end = '')
c = input()
a = int(c)
finished = False
while not finished:
        print ('Enter the next number (0 to finish): ', end ='')
        n = input()
        b = int(n)
        if b != 0:
            if b == a: 
                x = ('Same')
            elif b > a:
                x = ('Up')
            elif b < a:
                x = ('Down')
            a = b
            s = x
        else:
            finished = True

print (str(x))
