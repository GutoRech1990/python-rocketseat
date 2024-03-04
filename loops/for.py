# Enquanto uma condição for verdadeira

lista = [1,2,3,4,5]

for elemento in lista:
    print(elemento)

pessoa = {"nome": "Guto", "idade": 33}
for chave in pessoa.keys():
    print(chave)

for chave, valor in pessoa.items():
    print(chave,":",valor)


# range(): intervalo numérico
for number in range (10,21):
    print(number)


# enumerate():
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(indice, ":", valor)