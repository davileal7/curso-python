from openpyxl import Workbook, load_workbook

dados = load_workbook("cenprot.xlsx")
aba_ativa = dados.active
aba_ativa["A1"]
for celula in aba_ativa["A"]:
    print(celula.value)
