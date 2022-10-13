sexo = str(input("Informe seu sexo [M/F]")).strip().upper()
while sexo not in "MmFf":
   sexo = str(input("Dados inválidos. Por favor, informe novamente:")).strip().upper()
print("Sexo {} registrado com sucesso".format(sexo))
