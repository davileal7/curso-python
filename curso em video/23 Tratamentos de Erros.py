try: #(TENTAR)
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a/b
except Exception as  erro: #(SE DER PROBLEMA) - Falhou
    print(f'Problema encontrado foi >>> {erro.__class__}.')
except (ValueError,TypeError):
    print('Tivemos um problema com os dados digitados')
except ZeroDivisionError:
    print('NÃO é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('Não foi informado nada!!!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #(DEU CERTO)
    print(f'O resultado é {r:.1f}')
finally: #(CERTO/FALHA)
    print('Volte sempre! vlw')
