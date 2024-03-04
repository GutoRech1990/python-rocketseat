# Coleção não ordenada 

pessoa = {"nome": "Guto", "Idade": 33, "Cidade": "Luxembourg"}
print(pessoa)

# Acessar valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["Idade"])
print("Cidade:", pessoa["Cidade"])
print(20 * "-")

# Para adicionar novo item ao dicionario
pessoa["Sexo"] = "Masculino"
print(pessoa)

# Para alterar algum valor
pessoa["Idade"] = 32
print(pessoa)

# Para remover uma chave/valor
del pessoa["Sexo"]
print(pessoa)

# Métodos: keys(), values(), items()
chaves = pessoa.keys()
print(chaves)

valores = pessoa.values()
print(valores)

itens = pessoa.items()
print(itens)

# Para transformar em lista
itens = list(pessoa.items())
print(itens[0])
print(f"Nome: {itens[0][1]} -Idade: {itens[1][1]}")