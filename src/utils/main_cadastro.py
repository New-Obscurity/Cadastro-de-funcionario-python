from .delete_dice.banco_dados import lista_func
from .delete_dice.banco_dados import registrar_id

def cadastrar_funcionario():
    print("\n Cadastro de Funcionários \n")
    while True:
        
        global id_global
        id_global = registrar_id()  # Obtém o ID global inicial
        lista_funcionario = lista_func()



        print("")
        # declarei a variavel global para depois poder alterar os id
        # evitando assim ID de usuario repetido vai ficar sempre somando + 1
        nome = input("Nome: ")
        setor = input("Setor: ").strip()
        salario = float(input("Salŕio: ").strip())

        if salario < 0:
            print("Valores Negativos não são aceitos")
            continue

        else:
            funcionario = {
                "id": id_global,
                "nome": nome,
                "setor": setor,
                "salario": salario
                }
            print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: R$ {funcionario['salario']:.2f}\n")
            
            # Salva uma cópia do funcionário para evitar mudanças futuras
            # ele esta pegando o cadastro feito aqui e adicionando na lista funcionario??? que lista é essa?
            # a lista funcionario é a lista que esta no arquivo dados_funcionarios.py mas essa lista se chama lista_funcionario e não só funcionario
            lista_funcionario.append(funcionario.copy())
            id_global += 1

            sair = input("Deseja cadastrar outro funcionário? (S/N): ").strip().upper()
            if sair != "S" and sair != "SIM":
                print("Cadastro finalizado.")
                break