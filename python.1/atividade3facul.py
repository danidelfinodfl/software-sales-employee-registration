#print c meu nome
print("Bem vindos a Fábrica de Camisetas da Danielle")

def escolha_modelo():
    #vai perguntar o modelo desejado e retorna o valor do modelo
    while True:
        modelo = input("Digite o modelo desejado (MCS/MLS/MCE/MLE): ")
        if modelo not in ["MCS", "MLS", "MCE", "MLE"]:
            print("Opção de modelo inválida. Tente novamente.")
            continue
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        else:  # modelo == "MLE"
            return 3.20

def num_camisetas():
    #pergunta o número de camisetas e retorna o número de camisetas com desconto
    while True:
        try:
            num_camisetas = int(input("Digite o número de camisetas: "))
            if num_camisetas > 20000:
                print("Número de camisetas não aceito. Tente novamente.")
                continue
            if num_camisetas < 20:
                return num_camisetas
            elif 20 <= num_camisetas < 200:
                return num_camisetas * 0.95
            elif 200 <= num_camisetas < 2000:
                return num_camisetas * 0.93
            else:  # num_camisetas >= 2000
                return num_camisetas * 0.88
        except ValueError:
            print("Valor não numérico. Tente novamente.")

def frete():
    #pergunta pelo serviço adicional de frete e retorna o valor de frete
    while True:
        frete_opcao = input("Digite a opção de frete (1/2/0): ")
        if frete_opcao not in ["1", "2", "0"]:
            print("Opção de frete inválida. Tente novamente.")
            continue
        if frete_opcao == "1":
            return 100
        elif frete_opcao == "2":
            return 200
        else:  # frete_opcao == "0"
            return 0

#main
try:
    modelo_valor = escolha_modelo()
    num_camisetas_valor = num_camisetas()
    frete_valor = frete()
    total = (modelo_valor * num_camisetas_valor) + frete_valor
    print(f"Total a pagar: R${total:.2f}")
except Exception as e:
    print(f"Erro: {e}")

