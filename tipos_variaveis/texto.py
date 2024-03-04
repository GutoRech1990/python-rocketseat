# Declarar vairáveis

nome_completo = "Guto Rech"
print (nome_completo)

# Formatação
print(f"Nome completo: {nome_completo.upper()}")
print(f"Nome completo: {nome_completo.count("e")}")
print(f"Nome completo: {nome_completo.replace("h", "t")}")

telefone = "(47) 99999-9999"
print(telefone.replace("(", "").replace(")", "").replace("-", ""))

texto = "Guto"
texto = "-".join(texto)
print(texto)
print(texto.startswith("G"))
print("G-" in texto)
print("G-" not in texto)