#4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

#Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?


wt = False

while not wt:
    print("Descubra qual interruptor da sua sala")
    print("\n1 - interruptores")
    print("2 - interruptores")
    print("3 - interruptores\n")
    for k in range(2):
        op = int(input("Digite o numero correspondete:"))
        if op == 1:
            print("\n\033[91mNada acontece.\033[0m\n")
        elif op == 2:
            print("\n\033[92mLuz Acende.\033[0m\n")
            wt = True
        elif op == 3:
            print("\n\033[91mNada acontece.\033[0m\n")
        if op >= 4 :
            print("\n\033[93mNumero incorreto\033[0m\n")
    