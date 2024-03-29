import os

while True: # loop do recomeçar

    list_values = []

    def adicao(number_one,number_two):
        calc = (number_one + number_two)
        return calc

    def subtracao(number_one,number_two):
        calc = (number_one - number_two)
        return calc

    def multiplicacao(number_one,number_two):
        calc = (number_one * number_two)
        return calc

    def divisao(number_one,number_two):
        calc = (number_one / number_two)
        return calc

    def default():
        return ("Digito inválido")
        
    acconts = { # opções exibidas na tela
        "adição":1,
        "subtração":2,
        "multiplicação":3,
        "divisão":4,
    }

    print("Seja Bem-Vindo a sua Calculadora Básica!📲\n")

    for chave,valor in acconts.items(): # exibição das opções na tela
        print(f"{valor}) {chave}")

    while True: # loop de dígitos inválidos
        try: # validação para entrar somente input's de números
            response_users = int(input("\nMe informe por gentileza qual operação será usada:"))
        except ValueError:
            print("Digite somente números!")
            continue

        if response_users == 1:
            for i in range(2):
                while True: # loop da verificação de input
                    try: # validação para entrar somente input's de números
                        value = float(input(f"Digite o {i+1}° valor da soma: "))
                        list_values.append(value)
                        break
                    except ValueError:
                        print("Digite somente números!")
                        continue

            response_program = adicao(list_values[0],list_values[1])
            break # fim do loop de dígitos inválidos

        elif response_users == 2:
            for i in range(2):
                while True:
                    try:        
                         value = float(input(f"Digite o {i+1}° valor da subtração: "))
                         list_values.append(value)
                         break
                    except ValueError:
                        print("Digite somente números!")
                        continue

            response_program = subtracao(list_values[0],list_values[1])
            break # fim do loop de dígitos inválidos

        elif response_users == 3:
            for i in range(2):
                while True:
                    try:
                        value = float(input(f"Digite o {i+1}° valor da multiplicação: "))
                        list_values.append(value)
                        break
                    except ValueError:
                        print("Digite somente números!")
                        continue

            response_program = multiplicacao(list_values[0],list_values[1])
            break # fim do loop de dígitos inválidos

        elif response_users == 4:
            for i in range(2):
                while True:
                    try:
                        value = float(input(f"Digite o {i+1}° valor da divisão: "))
                        list_values.append(value)
                        break
                    except ValueError:
                        print("Digite somente números!")
                        continue

            response_program = divisao(list_values[0],list_values[1])
            break # fim do loop de dígitos inválidos
        else:
            print("Digito inválido!")
            continue

    print(f"Resultado: {response_program:.2f}")

    refresh = input("Deseja continuar?").upper().startswith("S")

    if refresh:
        print()
        os.system("cls")
        continue
    else:
        print("Valeu")
        break
