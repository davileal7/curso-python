from time import sleep
matriz = [[0,0,0],[0,0,0],[0,0,0]]
          #0#1#2  #0#1#2  #0#1#2
             #0      #1     #2
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para ({l}),({c}):"))
print("-"*40)
print("  C1     C2     C3")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c] %2==0:
             spar += matriz[l][c]
    print()
sleep(2)
print("-"*40)
print(f"A soma dos números pares é: {spar}.")
for l in range(0,3):
    scol += matriz[l][2]
print(f"A soma do valores da terceira coluna: {scol}.")
for c in range(0,3):
    if c == 0:
        mai = matriz[1][0]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é: {mai}.")