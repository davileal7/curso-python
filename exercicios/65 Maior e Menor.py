resp = "S"
soma = quantidade = média = maior = menor = 0
while resp in "Ss":
   n = int(input("Digite um número:"))
   soma += n
   quantidade += 1
   if quantidade == 1:
       maior = menor = n
   else:
       if n > maior:
           maior = n
       if n < menor:
           menor = n
   resp = str(input("Quer continuar [S/N] ?")).upper().strip()[0]
média = soma / quantidade
print("Você digitou \033[31m{} números\033[m e a média foi {}.".format(quantidade,média))
print("O maior número foi {} e o menor digitado foi {}.".format(maior,menor))
print("OBRIGADO!")