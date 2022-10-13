lista = []
for a in range(0,5):
    n = int(input("Digite um valor:"))
    if a == 0 or n > lista[-1]:
        lista.append(n)
        print("O valor foi adcionado para o fim da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print("O valor foi para o inicio da lista.")
                break
            pos += 1
print(f"Os valores digitados foram {lista}.")

