import random

def adivinhacao_jogo():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        tentativa = input("Faça sua tentativa: ")
        
        # Verifica se a entrada é um número
        if not tentativa.isdigit():
            print("Por favor, insira um número válido.")
            continue

        tentativa = int(tentativa)
        tentativas += 1

        if tentativa < numero_secreto:
            print("O número é maior que", tentativa)
        elif tentativa > numero_secreto:
            print("O número é menor que", tentativa)
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

# Executa o jogo
adivinhacao_jogo()
