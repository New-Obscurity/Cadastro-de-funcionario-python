import json

x = input("Aluno: ")
y = input("serie: ")
z = input("sexo: ")

d_test = {
    'aluno': x,
    'Semestre': y,
    'sexo': z
    }

# se for um dicionario tem que carregar ele antes 
# para o json poder ler aparentemente

json.load = d_test

print(d_test)
print("\n")

# Sort key ajuda a separar o dicionario por chaves
# enquanto o indent recua a quantidade de espaços definidas nele
print(json.dumps({d_test}, indent=4))