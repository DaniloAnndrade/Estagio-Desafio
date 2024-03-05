#3) Descubra a lógica e complete o próximo elemento:

#a) 1, 3, 5, 7, ___

cont = 0

for b in range(20):
    cont += 1
    if cont % 2 == 1:
        print(cont, end="-")


# Resposta: Numeros Impar
print("\nResposta: Numeros Impar")
print("\nfim\n")


#b) 2, 4, 8, 16, 32, 64, ____

cont2 = 0

for b in range(100):
    cont2 += 1
    if cont2 % 2 == 0:
        print(cont2, end="-")
# Resposta: Numeros par
print("\nResposta: Numeros par")
print("\nfim\n")

#c) 0, 1, 4, 9, 16, 25, 36, ____
        
cont3 = 0

for c in range(100):
    cont3 += 1
    if cont3 ** (1/2) == int(cont3 ** (1/2)):
        print(cont3, end="-")

# Resposta: RAiz Quadrada
print("\nResposta: Raiz Quadrada")
print("\nfim\n")  

#d) 4, 16, 36, 64, ____

sequencia = 0

for i in range(1, 10 + 1):
    sequencia = (2 * i) ** 2
    print(sequencia, end="-")

# Resposta: Progressão Aritmética
print("\nResposta: Progressão Aritmética")
print("\nfim\n")  

#e) 1, 1, 2, 3, 5, 8, ____
        
num = 0
num2 = 1
print(num2, end="-")
for e in range(10):
    soma2 = num +num2
    num = num2
    num2 = soma2     
    print(soma2, end="-")

# Resposta: Fibonacci
print("Resposta: Fibonacci")
print("\nfim\n")  

#f) 2,10, 12, 16, 17, 18, 19, ____

x = 2
y = 10
w = x + y
print(x, end="-")
print(y, end="-")
for f in range(w, 50, 2):
    print(f, end="-")

# Resposta: Progreção de 2 em 2 apartir da soma de 2 numeros
print("\nResposta: Progreção de 2 em 2 apartir da soma de 2 numeros")