#Triangulo de asteriscos 
n=5
for i in range(1, n + 1):
    print("*" * i)

print(" ")


#Triangulo invertido
for i in range (n, 0, -1):
    print("*" * i)


print(" ")
#Piramide centrada
for i in range(1, n + 1):
    espacios = " " * (n - i)
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)
    
