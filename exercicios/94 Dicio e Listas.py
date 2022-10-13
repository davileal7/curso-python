galera = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print("ERRO! Tente novamente.")
    pessoa['Idade'] = int(input("Idade: "))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if r in'SN':
            break
        print('ERRO! Tente novamente.')
    if r in 'N':
        break
print("-=-"*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As Mulheres cadastradas foram', end=" ")
for p in galera:
    if p['Sexo'] in "Ff":
        print(f'{p["Nome"]}', end=" ")
print()
print('D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['Idade'] >= média:
        print(' ', end="")
        for k, v in p.items():
            print(f"{k} = {v};", end= "")
        print()
print("ENCERRADO")

