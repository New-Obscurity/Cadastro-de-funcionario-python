from utils import cadastrar_funcionario
from utils import consultar_funcionarios
from utils import remover_funcionario
# importando as funções de cada arquivo/menu


open("armazenamento.txt", "w").close()  # Limpa o arquivo de armazenamento


# Menu Principal
while True:


    # Utilizei um dicionário para o menu tornando das chaves strings fica fácil
    # de limitar a entrada do usuário pois qualquer valor diferente das chaves
    # irá gerar uma mensagem de erro.
    menu_ui = {
    "1": "Cadastrar Funcionários",
    "2": "Consultar Funcionário(s)",
    "3": "Remover Funcionário",
    "4": "Encerrar Programa"
    }


    # Exibindo o menu
    print("\n Selecione a ação desejada: \n")


    # aqui eu defini o nome da chave como "numero_entrada" e o valor como "lugar"
    for numero_entrada, lugar in menu_ui.items():


        # Aqui exibo o número de entrada e o lugar correspondente
        print(f"{numero_entrada} - {lugar}")


    # fora da estrutura de repetição, para evitar repetir o espaço em branco em cada iteração    
    print("")


    # Entrada do usuário posso melhorar a validação visualmente creio eu
    opcao = input("Opção: ").strip()


    # como todo dado de entrada se torna uma string logo incluindo os numeros
    # torno a validação mais fácil, pois qualquer valor diferente das chaves
    # irá gerar uma mensagem de erro como eu disse antes
    if opcao == "1":
        cadastrar_funcionario()

            
    elif opcao == "2":
        consultar_funcionarios()


    elif opcao == "3":
        remover_funcionario()


    elif opcao == "4":
        break

            
    else:
        print("Dado invalido. Tente novamente")
        print("")