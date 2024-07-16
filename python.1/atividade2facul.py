#meu nome e o menu
print("------ Bem-vindo a Loja de Marmitas da Danielle -----------")
print("------------------------------Menu!--------------------------")
print("----------------------------------------------------------------")
print("---| Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---")
print("---|    P     |       R$ 16.00       |       R$ 15.00       |---")
print("---|    M     |       R$ 18.00       |       R$ 17.00       |---")
print("---|    G     |       R$ 22.00       |       R$ 21.00       |---")
print("----------------------------------------------------------------")


#inicializa
total_pedido = 0

while True:
    #input do sabor
    sabor = input("Digite o sabor (BA/FF): ")
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        continue

    #tamanho
    tamanho = input("Digite o tamanho (P/M/G): ")
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue

    #aqui calcula o valor do pedido
    if sabor == "BA":
        if tamanho == "P":
            valor_pedido = 16
        elif tamanho == "M":
            valor_pedido = 18
        else:  # tamanho == "G"
            valor_pedido = 22
    else:  # sabor == "FF"
        if tamanho == "P":
            valor_pedido = 15
        elif tamanho == "M":
            valor_pedido = 17
        else:  # tamanho == "G"
            valor_pedido = 21

    #aqui adiciona o valor do pedido ao acumulador
    total_pedido += valor_pedido

    #pergunta se deseja pedir mais alguma coisa
    resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
    if resposta.upper() == "N":
        break

# total do pedido
print(f"Total do pedido: R${total_pedido:.2f}")
