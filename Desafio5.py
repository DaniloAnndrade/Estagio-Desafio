#5) Escreva um programa que inverta os caracteres de um string.

#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
print("Escreva um nome, é veja ele ao contrario.")
pal = str(input("Digite um nome:")).upper()

#b) Evite usar funções prontas, como, por exemplo, reverse;

for k in range(len(pal)-1,-1,-1):
    print(pal[k], end=" ")