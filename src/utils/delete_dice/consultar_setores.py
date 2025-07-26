import json


def consultar_setor():
    print("\n Consulta por setor \n")

    while True:
        encontrado = False
        try:
            area = input("Insira o setor: ").strip().upper()

            for funcionario in dados():
                if area == funcionario['setor']:
                    encontrado = True
                    print(f"Setor: {funcionario['setor']} | ID: {funcionario['id']} | Nome: {funcionario['nome']} | Salário: R$ {funcionario['salario']:.2f}")
            if encontrado != True:
                print("Setor não encontrado")

            # evita loop infinito
            continuar = input("Deseja buscar outro setor?? (S/N): ").strip().upper() # retira os espaços e deixa em caixa alta
            if continuar != "S":
                break
            
        except ValueError:
            print("Dado inexistente. Tente Novamente")