print("                     ")


c = int(input("Ingresa el capital : "))

n = 0
d = 2*c

while (c < d):
    c = c*0.05+c
    n = n + 1
    print("mes = " , str(n))
    print("capital = " , str(c))

print("Los meses son " , str(n))
