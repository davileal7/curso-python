jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador:'))
    tot = int(input(f'Quantas partidas{jogador["Nome"]} jogou?'))
    partidas.clear()
    for a in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {a+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Tente novamente.')
    if r == 'N':
        break
print('-=-'*30)
print('Cod', end="")
for i in jogador.keys():
    print(f' {i:<15}',end="")
print()
print('-=-'*30)
for a,b in enumerate(time):
    print(f' {a:>3}', end="")
    for d in b.values():
        print(f'{str(d):<15}',end="")
    print()
print('-=-'*30)
while True:
    busca = int(input("Mostrar daddos de qual jogador?(999 STOP)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! NÃO existe esse jogador {busca}!')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for a,b in enumerate(time[busca]['gols']):
            print(f' No jogo {a+1} fez {b} gols.')
    print('-=-' * 30)
print("ENCERRADO")
