from random import randint

print("="*50)
v=0
while True:
    j = int(input("Digite um valor:"))
    c = randint(0,10)
    total = j + c
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar?")).strip().upper()[0]
    print(f"Você jogou {j} e o cumputador {c}.Total de {total}.")
    if tipo == "P":
        if total % 2==0:
            print("Você VENCEU")
            v += 1
        else:
            print("Você PERDEU")
            break
    elif tipo == "I":
        if total % 2==1:
            print("Você VENCEU")
            v += 1
        else:
            print("Você PERDEU")
            break
    print("Vamos jogar novamente...")
print(f"Game Over! Você Venceu {v} vezes.")

