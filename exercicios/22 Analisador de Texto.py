nome = str(input("Digite um nome completo:")).strip()
print("\033[1;33m----Analisando seu nome----")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0],len(separa[0])))
print("Seu segundo nome é {} e tem {} letras".format(separa[1],len(separa[1])))
print("Seu terceiro nome é {} e tem {} letras".format(separa[2],len(separa[2])))
print("Seu quarto nome é {} e tem {} letras".format(separa[-1],len(separa[-1])))













