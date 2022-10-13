nome = str(input("\033[33mQual é o seu nome?\033[m")).strip().upper().lower()
if nome == "davi":
    print("\033[34mOpa! ai sim que nome abençoado...\033[m")
elif nome == "pedro" or nome == "maria" or nome == "paulo":
    print("Seu nome é bem popular aqui no Brasil.")
elif nome in "naara":
    print("\033[35mQue belo nome você tem, que mulher virtuosa\033[m.")
else:
    print("Seu nome é bem normal")
print("Prazer em te conhecer {}".format(nome.upper()))
print("Tenha um ótimo dia,que Deus te abençoe,cuide-se {}".format(nome.upper()))
print("Fica com Deus")
print("E até a próxima!")
