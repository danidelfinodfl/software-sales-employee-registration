#Meu nome
print("Bem-vindos à loja da Danielle Delfino")

#Entrada do valor do pedido e da quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

#Inicialização da taxa de juros
taxaJuros = 0

#Estrutura condicional para definir a taxa de juros
if quantidadeParcelas < 4:
    taxaJuros = 0  # Sem juros
elif 4 <= quantidadeParcelas < 6:
    taxaJuros = 0.04  # Juros de 4%
elif 6 <= quantidadeParcelas < 9:
    taxaJuros = 0.08  # Juros de 8%
elif 9 <= quantidadeParcelas < 13:
    taxaJuros = 0.16  # Juros de 16%
else:
    taxaJuros = 0.32  # Juros de 32%

#Cálculo do valor da parcela e do valor total parcelado
valorDaParcela = (valorDoPedido * (1 + taxaJuros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#Saída de console com o parcelamento e juros
print(f"O valor das parcelas é de: R${valorDaParcela:.2f}")
print(f"O valor Total Parcelado é de: R${valorTotalParcelado:.2f}")
