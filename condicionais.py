#  if, elif, else

# Exemplo de if
idade = int(input("Qual idade? "))

if idade >= 18:
    print("Maior de 18")
elif idade >=16 and idade<18:
    print("Relativamente capaz")
if idade != 10:
    print("Não é 10")
else:
    print("Menor de 18")


msg = "Tem 18" if idade == 18 else "Não tem 18"
print(msg)