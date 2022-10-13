matriz = [[0,0,0],[0,0,0],[0,0,0]]
          #0#1#2  #0#1#2  #0#1#2
             #0      #1     #2
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para ({l}),({c}):"))
print("-"*40)
print("   C1     C2     C3")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
