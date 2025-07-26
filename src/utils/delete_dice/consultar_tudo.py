dados = open("armazenamento.txt", "r")

def consultar_todos():
    print("\n Consulta de Todos os Funcionarios \n")
    for funcionario in dados():
        print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: R$ {funcionario['salario']:.2f}")
