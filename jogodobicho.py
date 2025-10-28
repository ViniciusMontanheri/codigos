import random
bicho = ["🐶","🐭","🐷","🐻","🐰","🐱"]
saldo = float(input("Faça um deposito para comçar a jogar: "))
print("🐯JOGO DO BICHO🐯")
print("~"*100)
while saldo > 0:
    print(f"Saldo atual: ${saldo}")
    aposta = float(input("Quanto quer apostar? (Digite 0 para sair) "))
    if aposta == 0:
        print(f"Seu saldo final foi de {saldo}, até mais!")
        break
    saldo = saldo - aposta
    sorteio = [random.choice(bicho) for _ in range(3)]
    print("Resultado:"," / ".join(sorteio))

    if sorteio[0] == sorteio[1] == sorteio[2]:
        print(f"3 frutas iguais! você ganhou {aposta * 5}")
        saldo = saldo + aposta * 5
    elif sorteio [0] == sorteio [1] or sorteio[1] == sorteio[2]:
        saldo = saldo + aposta * 2
    else:
        print('Não ganhou nada 😭')

    print("-" * 40)

    if saldo <= 0:

        print("Seu dinheiro acabou")
