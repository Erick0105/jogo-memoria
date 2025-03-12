import random, time, os

led_array = [1,2,3,4,5]
led_array_escolhidos = []

    
while True:
    led_sortido = random.choice(led_array)
    
    led_array_escolhidos.append(led_sortido)
    contador = 0
    for i in led_array_escolhidos:
        contador += 1
        print(f'{contador}º número - {i}')
        time.sleep(1.5)
        os.system('cls')
    
    valor_digitado = int(input("Qual foi o ultimo valor que apareceu?"))
    if valor_digitado == led_array_escolhidos[-1]:
        print("Parabéns você acertou, vamos continuar")
        time.sleep(2)
        os.system('cls')
    else:
        print("Você errou que pena")
        break