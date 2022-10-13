# def / função - criar comandos personalizados / rotina

def linha():
    print("-" * 30)
# Teste 1 - Programa Principal
linha()


# print("---Sistema de Alunos---")
# linha()
# print("Cadastro de Funcionários")
# linha()


def título(txt):  # (txt) PARÂMETRO
    print(txt)
# Teste 2 - Programa Principal
título("Curso em Video")  # (txt)
título("Oi, Mundo!")      # (txt)



def soma(a, b):
    s = a + b
    print(s)
    print(f"A soma de {a} + {b} é = {s}")
# Teste 3 - Programa Principal
soma(2, 10)  # a,b
soma(5, 2)  # a,b


def contador(*num):  # *desempacotar
    for valor in num:
        print(f' {valor}', end=" ")
    tam = len(num)
    print()
    print(f"Recebi os valores {num} e no total são {tam} números.")


contador(2, 4, 6)
contador(3, 3, 5, 99, 1)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 3, 5]
dobra(valores)
print(f'DOBRA {valores}.')


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}.")


soma(5, 2)
soma(3, 2, 6)
