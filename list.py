import os
import pandas as pd

lista = os.listdir("/home/brunomelo/Documentos/Vendas")
tabelatt = pd.DataFrame()
for cd in lista:
    if 'Vendas' in cd:
        tabela = pd.read_csv(f'/home/brunomelo/Documentos/Vendas/{cd}')
        tabelatt = tabelatt.append(tabela)

tabelatt['Faturamento']=tabelatt['Quantidade Vendida']*tabelatt['Preco Unitario']
tbprod = tabelatt.groupby('Produto').sum()
print(tbprod[["Quantidade Vendida"]].sort_values(by='Quantidade Vendida',ascending=True))
tbfat = tabelatt.groupby('Produto').sum()
print(tbfat[["Faturamento"]].sort_values(by='Faturamento',ascending=True))
tbloja = tabelatt.groupby('Loja').sum()
print(tbloja[["Faturamento"]].sort_values(by='Faturamento',ascending=True))