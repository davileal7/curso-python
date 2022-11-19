def fim_de_semana(dia):
    match dia:
        case 'Domingo' | 'Sábado':
            return "Fim de semana"

        case _:
            return 'Dia Útil'

print(fim_de_semana('Sábado'))
print(fim_de_semana('Segunda'))