def contas(centros):
    match centros:
        case [area, centros]: #apenas 1 centro de custo
            print(f'A área {area} possui o centro de custo {centros}')


        case [area, *centros]: #2 ou mais centros
            print(f'A área {area} possui os centros de custo abaixo:')
            for centro in centros:
                print(centro)

contas(['Financeiro', 'ABC'])  # 1° case
contas(['Marketing','ABC', 'XYZ', 'HJG']) # 2° case