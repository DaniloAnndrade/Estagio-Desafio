#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


# o numero e informado pelo Usuario. 

num = 0
num2 = 1

usu = int(input("Digite um numero:"))

wtrue = False

# O programa Verifica se ele e Fibonacci.

while not wtrue:

    soma2 = num +num2
    num = num2
    num2 = soma2
    if soma2 == usu:
        print(f"O numero {usu} digitado faz parte de Fibonacci.")
        wtrue = True
    elif soma2 > usu:
        print(f"O numero {usu} digitado não faz parte de Fibonacci.")
        wtrue = True
            
# No final e informado o resultado.