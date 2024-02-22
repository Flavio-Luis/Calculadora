condicao = True

while condicao:
    try :
        numero_um = float(input("\nDigite o primeiro valor: "))
        numero_dois = float(input("Digite o segundo valor: "))
        operador = input("Digite a operação que deseja: ")

        if operador == "+":
            resultado = numero_um + numero_dois
        elif operador == "-":
            resultado = numero_um - numero_dois
        elif operador == "/":
            resultado = numero_um / numero_dois
        elif operador == "*":
            resultado = numero_um * numero_dois
                    
        print(f"Sua conta de {numero_um} {operador} {numero_dois} = {resultado:.2f}")

    except :
        print("Você não digitou um dos valores corretamente! ")
        print("OBS: os operadores aceitos são +(adição), -(subtração), /(divisão)" \
              "*(multiplicação)")
    
    resposta = input("Deseja recomeçar ?")
    resposta = resposta.lower()
    resposta = resposta.startswith("s")

    if resposta is False:
        print("Até Mais!\n")
        break


    