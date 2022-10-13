times = ("Corinthians", "Palmeiras","São Paulo","Santos","Flamengo","Atlético MG",
         "Fluminense","Internacional","Fortaleza","Chapecoense",
         "Sport","Coritiba","Cruzeiro","Vasco","Bahia","Grêmio",
         "América MG","Botafogo")
print("=" * 60)
for a in times:
    print(a)
print("=" * 60)
print(f"\033[34mClassificação para libertadores: {times[0:4]}\033[m")
print("=" * 60)
print(f"O oitavo time na classificação é: {times[7]} ")
print("=" * 60)
print(f"\033[31mZona de rebaixamento: {times[-4:]}\033[m")
print("=" * 60)
print(f"Ordem alfabética:{sorted(times)}")