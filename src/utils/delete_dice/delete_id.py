dados = open("armazenamento.txt", "r+")

# função consultar_id
def consultar_id():

    # definindo a variavel "encontrado" como False para verificar se o ID foi encontrado ou não
    encontrado = False
    
    # printando o titulo da consulta
    print("")
    print("Consulta por ID")
    print("")

    # um loop infinito para continuar perguntando ao usuario se ele deseja buscar outro ID
    while True:
       
       # tenta capturar o ID do funcionario se ensirir algo que não seja um número inteiro
       # vai gerar um ValueError e o programa vai avisar que o dado é inexistente e vai pedir para tentar novamente
        try:
          
          # a variavel "pesquisa" armazena o ID do funcionario que o usuario deseja pesquisar
            pesquisa = int(input("Insira o ID do  funcionario: "))
          
          # apenas estetica
            print("")

            # percorre a lista de funcionarios e verifica se o ID inserido pelo usuario existe
            for funcionario in dados():
                
                # se o ID existir na lista de funcionarios mudara a variavel encontrado para True
                # e printara os dados do funcionario
                if pesquisa == funcionario['id']:

                    # mudando a variavel encontrado para True
                    encontrado = True

                    # printando os dados do funcionario que estão dentro da "lista_funcionario" que tem o dicionario funcionario
                    print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: R$ {funcionario['salario']:.2f}")

                # estetica tambem
                print("")

            # se a variavel que definimos antes "encontrado" continuar False
            if encontrado != True:

                # printa que o ID não foi encontrado
                print("ID não encontrado")

                # outra parte estetica
                print("")


            # com o id encontrado ou não, o programa pergunta se o usuario deseja buscar outro ID
            # na variavel que vai receber a resposta do usuario padroniza dois tipos de resposta
            continuar = input("Deseja buscar outro ID? (s/n): ").strip().upper() # ela retira os espaços e deixa em caixa alta

            print("")

            # qualquer resposta diferente de "S" ou "SIM" vai sair do loop
            # e o programa vai finalizar a consulta por ID
            if continuar != "S":

                break

        # se o usuario inserir algo que não seja um numero inteiro o programa vai gerar um ValueError
        # e vai printar que o dado é inexistente e pedir para tentar novamente
        except ValueError:

            print("Dado inexistente. Tente Novamente")