nome = str(input("Qual é o seu nome?")).upper().lower().strip()
if nome == "davi" :
    print("\033[1;33mPo legal!!! que nome bacana você tem...")
else:
    print("Olá! Prazer tudo bem?")
print("\033[1;36mTehna um bom dia!!! {}".format(nome.upper()))