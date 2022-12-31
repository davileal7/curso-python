from time import sleep

def contador(i,f,p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print("="*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.5)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.5)
            cont -= p
        print()
#Programa Principal
contador(1,10,1) #inicio,fim,passo
contador(10,0,2)
print("="*20)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Ínicio:"))
f = int(input("Fim:"))
p = int(input("Conta de:"))
contador(i,f,p)

