primeiro = int(input("Primeiro termo:"))
razão = int(input("Razão:"))
décimo = primeiro + (9) * razão
for c in range(primeiro, décimo + razão, razão):
    print("{}".format(c), end= " > ")
print()
print("ACABOU!")
