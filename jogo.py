print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")

numerosecreto = 40

chute = input("Digite o seu número: ")
print("você digitou: ",chute)

chuteNumerico = int (chute)

acertou = chuteNumerico == numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto


#se voce digitar qualquer numero vou verificar se acertou ou errou
if(numerosecreto==chuteNumerico):
    print("Você acertou!")
else:
     print("Você errou!")

print("fim do jogo")