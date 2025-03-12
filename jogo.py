import random, time, os

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')
        
def validar_num(text) -> int:
    texto_erro = ""
    while True:
        try:
            possivel_num = int(input(texto_erro + text))
            break
        except:
            texto_erro = "Por favor digite um número inteiro\n" 
    return possivel_num

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
        limpar_terminal()
    
    valor_digitado = validar_num("Qual foi o ultimo valor que apareceu?\n=> ")
    if valor_digitado == led_array_escolhidos[-1]:
        print("Parabéns você acertou, vamos continuar")
        time.sleep(2)
        limpar_terminal()
    else:
        print("Você errou que pena")
        break