ficha = []
while True:
    nome = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for a, b in enumerate(ficha):
    print(f"{a:<4}{b[0]:<10}{b[2]:>8.1f}")
while True:


    print("-"*30)
    opc = int(input("Mostrar notas de qual aluno? (999 encerra):"))
    if opc == 999:
        print("FINALIZADO")
        break
    if opc<= len(ficha) -1:
        print(f"Notas de {ficha[opc][0]} são: {ficha[opc][1]}")
print("<<<VOLTE SEMPRE>>>")
