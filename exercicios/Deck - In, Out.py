def linha():
    print('='*50)
linha()
Uw = ["2x Dovin Veto","1x Elpeth"]
Burn = ["2x Layline","2x Dovin Veto"]
Ds = ["2x Layline", "2x Celestial Purge"]
Ur = ['2x Rest in Peace', "1x Veredito",'1x Push']
LivingEnd = ['2x Rest in Peace','1x Veredito','2x Dovin Veto']
while True:
    match = str(input("Qual a match será contra? [Uw, Burn ,Ds ,Ur ,LivingEnd]: ")).capitalize()
    if match == "Uw":
        print("\033[33mEntra as seguintes cartas:\033[m")
        print(Uw)
    elif match == "Burn":
        print("\033[33mEntra as seguintes cartas:\033[m")
        print(Burn)
    elif match == "Ds":
        print("\033[33mEntra as seguintes cartas:\033[m")
        print(Ds)
    elif match == 'Ur':
        print("\033[33mEntra as seguintes cartas:\033[m")
        print(Ur)
    elif match == 'LivingEnd':
        print("\033[33mEntra as seguintes cartas:\033[m")
        print(LivingEnd)
    else:
        print('\033[32mErro! Digite apenas as opções anteriores.\033[m')
    linha()
    r = str(input("Quer continuar? [S/N]")).strip()
    if r in "Nn":
        break
linha()
print("FIM")






