import random

print("********************************")
print("Bem-vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randint(1, 100)
tentativas_restantes = 10

while tentativas_restantes > 0:
    print(f"Você tem {tentativas_restantes} tentativas restantes.")
    chute = input("Qual é o seu chute? ")

    try:
        chute_numerico = int(chute)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if chute_numerico == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break

    if chute_numerico > numero_secreto:
        print("Você errou! Seu chute foi maior que o número secreto.")
    else:
        print("Você errou! Seu chute foi menor que o número secreto.")

    tentativas_restantes -= 1
    if tentativas_restantes > 0:
        print()

if tentativas_restantes == 0 and chute_numerico != numero_secreto:
    print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")

print("Fim do jogo")
