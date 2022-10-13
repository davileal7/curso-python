from random import randint
números = (randint(1, 20), randint(1, 20), randint(1, 20))
print(f"Os números sorteados foram:" , end="")
for n in números:
    print(f" {n} " ,end="")
print(f"\nO MAIOR número foi: {max(números)}")
print(f"O MENOR número foi: {min(números)}")
if 10 in números:
    print("Você GANHOU!!!")
else:
     if 3 in números:
      print("PERDEU")
