dados = open("armazenamento.txt", "r+")

# Função para remover funcionário
def remover_funcionario():

    print("\n Remoção de Funcionário \n")


    # Verefica se há algum dado na lista para ser deletado
    if not dados():
        print("Não há dados para deletar")
        return


    while True:

        lista_funcionario = dados  # Obtém a lista de funcionários
        encontrado = False
        
        # evitar entrada de valores invalidos
        try:
            id_deletar = int(input('ID do funcionario a ser removido: ').strip()) # strip deve ser aplicado antes da conversão para int

            # Buscando dentro da lista tal ID
            for indice, funcionario in enumerate(lista_funcionario):

                if id_deletar == funcionario["id"]:
                    encontrado = True

                    print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: R$ {funcionario['salario']:.2f}\n")
                    print("Deseja realmente deletar? (Sim / Não)")

                    certificar = input("").strip().upper()
                    if certificar != "SIM":
                        continue

                    else:
                        del dados.lista_funcionario()[indice]
                        print("Funcionário removido com sucesso.")

            if encontrado == False:
                print("Funcionario não encontrado")
                
            continuar = input("Deseja remover outro? (S/N)").strip().upper()

            if continuar != "S":
                break



        except ValueError:
            print("Entrada Inválida")
