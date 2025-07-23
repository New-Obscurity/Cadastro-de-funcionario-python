from .banco_dados import lista_func

def consultar_todos():
    print("\n Consulta de Todos os Funcionarios \n")
    for funcionario in lista_func():
        print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: R$ {funcionario['salario']:.2f}")
