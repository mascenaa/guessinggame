from typing import Generator


print("***************************")
print("JOGO DE ADIVINHAÇÃO")
print("***************************")

 #import bankkai!
import random  

numero_secreto = round((random.randrange(1, 101)))
tentativas = 3
rodadas = 1

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
        tentativas = 20
elif (nivel == 2):
        tentativas = 10
else:
        tentativas = 5


for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodadas, tentativas))
    chute_string = input("Digite um número entre 1 e 100: ")
    chute = int(chute_string)
    print("Você digitou " , chute)

    if(chute < 1 or chute > 100):
        print("Você digitou um número errado, coloque um número de 1 a 100")
        continue

    acertou     = chute == numero_secreto
    errou_maior = chute > numero_secreto
    errou_menor = chute < numero_secreto

    if (acertou):
        print("Oba, você acertou!")
        break
    else: 
        if(errou_maior):
            print("Poxa, você errou! O seu chute foi maior que o número secreto...")
        elif(errou_menor):
            print("Poxa, você errou! O seu chute foi menor que o número secreto...")
    
    rodadas = rodadas + 1
    print("Woops! Fim de jogo. Tente novamente com outra ficha!")
    