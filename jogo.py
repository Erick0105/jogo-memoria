import random, time, os

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def verificarYesNo(text) -> str:
    msg_erro = ""
    while True:
        resposta = input(msg_erro + text + " (Y/N)\n=> ").upper()[0]
        if resposta not in ["Y",'N']:
            msg_erro = "Por favor digite 'Yes' ou 'No' para prosseguir\n"
        else:
            break
    return resposta
        
def validar_num(text, *args) -> int:
    texto_erro = ""
    while True:
        try:
            possivel_num = int(input(texto_erro + text))
            if not args:
                break
            else:
                if possivel_num not in args:
                    texto_erro = "Por favor digite um número dentro as opções\n"
                else:
                    break
        except:
            texto_erro = "Por favor digite um número inteiro\n" 
    return possivel_num

    
recorde = 0
while True:

    dificuldade = validar_num("Escolha a dificuldade desejada\n\n[1] - Fácil\n[2] - Normal\n[3] - Difícil\n\n=> ",1,2,3)

    match dificuldade:

        case 1:
            qtnd_nums = 3
            tempo = 3
        case 2:
            qtnd_nums = 5
            tempo = 1.5
        case 3:
            qtnd_nums = 7
            tempo = 0.2


    lista_nums = []
    num_array_escolhidos = []

    for x in range(qtnd_nums):
        lista_nums.append(x + 1)
    
    while True:
        contador = 0

        num_sortido = random.choice(lista_nums)

        num_array_escolhidos.append(num_sortido)
        for i in num_array_escolhidos:
            contador += 1
            print(f'{contador}º número - {i}')
            time.sleep(1.5)
            limpar_terminal()

        valor_digitado = validar_num("Qual foi o ultimo valor que apareceu?\n=> ")
        if valor_digitado == num_array_escolhidos[-1]:
            print(f"Parabéns você acertou,sua pontuação é de {contador} pontos vamos continuar")
            time.sleep(2)
            limpar_terminal()
        else:
            contador -= 1
            print(f"Você errou que pena, sua pontuação foi de {contador}")
            break

    if contador > recorde:
        recorde = contador
        print(f"Parabéns seu novo recorde é de {recorde} pontos")
    else:
        print(f"Que pena faltou {recorde - contador + 1} pontos para bater seu recorde")
    repeticao = verificarYesNo("Você deseja jogar de novo?")
    if repeticao == "N":
        print("Foi um bom jogo")
        break
    else:
        print("Então tenha uma boa sorte")