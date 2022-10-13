jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do Jogador:'))
tot = int(input(f'Quantas partidas{jogador["Nome"]} jogou?'))
for a in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {a+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-'*30)
for a,b in jogador.items():
    print(f'O campo{a} tem o valor {b}')
print('-=-'*30)
print(f'O jogador{jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for a,b in enumerate(jogador["gols"]):
    print(f"   => Na partida {a+1}, fez {b} gols.")
print(f'Foi um total de {jogador["total"]} gols.')


