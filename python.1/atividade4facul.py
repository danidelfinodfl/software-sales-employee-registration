#meu nome
print("Bem vindo a Empresa do Danielle")

#inicializado a lista de funcionários e id global
lista_funcionarios = []
id_global = 4297913

def cadastrar_funcionario(id):
   
    print(f"Id do Funcionário: {id}")
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    funcionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    lista_funcionarios.append(funcionario.copy())

def consultar_funcionarios():
    
    while True:
        opcao = input("Escolha a opção desejada:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\n>> ")
        if opcao == "1":
            for funcionario in lista_funcionarios:
                print(f"Id: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
        elif opcao == "2":
            id_consultar = int(input("Digite o id do funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id_consultar:
                    print(f"Id: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
                    break
            else:
                print("Id inválido")
        elif opcao == "3":
            setor_consultar = input("Digite o setor: ")
            for funcionario in lista_funcionarios:
                if funcionario["setor"] == setor_consultar:
                    print(f"Id: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
        elif opcao == "4":
            return
        else:
            print("Opção inválida")

def remover_funcionario():
    
    while True:
        id_remover = int(input("Digite o id do funcionário a ser removido: "))
        for funcionario in lista_funcionarios:
            if funcionario["id"] == id_remover:
                lista_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso!")
                return
        else:
            print("Id inválido")

#main
while True:
    opcao = input("Escolha a opção desejada:\n1. Cadastrar Funcionário\n2. Consultar Funcionário(s)\n3. Remover Funcionário\n4. Sair\n>> ")
    if opcao == "1":
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")
