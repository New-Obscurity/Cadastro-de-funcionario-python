from .delete_dice import consultar_setor
from .delete_dice import consultar_todos
from .delete_dice import consultar_id


def consultar_funcionarios():
    while True:
        print("\n Consulta de Funcionários: \n")

        menu_ui_2 = {
        "1": "Consultar Todos",
        "2": "Consultar por ID",
        "3": "Consultar por Setor",
        "4": "Retornar ao Menu"
        }

        # nome defenido a chave e valor
        for entrada, lugares in menu_ui_2.items():
            print(f"{entrada} - {lugares}")
        print("")

        opcoes = input("").strip()

        if opcoes == "1":
            consultar_todos()
            print("")
            
        elif opcoes == "2":
            consultar_id()
            print("")
            
        elif opcoes == "3":
            consultar_setor()
            print("")
            
        elif opcoes == "4":
            return # sai da função e volta pro menu principal

        else:
            print("Opção inválida")
            print()