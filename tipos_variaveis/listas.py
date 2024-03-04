# Uma coleção de elementos ordenados e mutáveis

minha_lista = [1,2,3,4,5, "Guto"]

print(minha_lista)

# Para acessar algum item da lista
print(minha_lista[5])

# Para acessar um intervalo de intens
print(minha_lista[1:4])

# Para substituir uma informação dentro da lista
minha_lista[0] = "Rech"
print(minha_lista)

# Para incluir algo na lista
minha_lista.append("José")
print(minha_lista)

# Para saber em que posição esta algum item da lista
indice_guto = minha_lista.index("Guto")
print(indice_guto)

# Para inserir um item em uma determinada posição ( não vai substituir o item na lista, e sim jogar o resto para frente)
minha_lista.insert(1, "Paulo")
print(minha_lista)

# Para excluir algum item em uma posição
minha_lista.pop(6)
print(minha_lista)

# Para organizar a lista - método sort
lista2 = [3,7,4,9,8]
lista2.sort()
print(lista2)