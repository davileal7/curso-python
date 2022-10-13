def ficha(jog="<Desconhecido>",gol=0):
    print(f'O jogador {jog} fez {gol}x gols no campeonato.')

n = str(input("Nome do jogador:"))
g = str(input("Quantos gols?"))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n,g)