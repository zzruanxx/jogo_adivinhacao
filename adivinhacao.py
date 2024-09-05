import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
while True: 
    chute = int(input("Adivinhe o numero entre 1 e 100: "))
    tentativas += 1 

    if chute < numero_secreto:
        print("Muito Baixo!")
    elif chute > numero_secreto:
        print("Muito Alto!")    
    else:
        print(f"Parabens, voce acertou o numero {numero_secreto} em {tentativas} tentativas")    
        break

    jogo_adivinhacao()

