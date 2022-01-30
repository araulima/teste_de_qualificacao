# -*- coding: utf-8 -*-

import pandas as pd 
dados = pd.read_excel('teste.xlsx')
saques = dados.loc[(dados["TRANSAÇÃO"] == 'SAQUE CASH/ATM BB')]

nomes = saques['NOME PORTADOR']

x = []
for i in nomes:
 if i not in x:
  x.append(i)

z = []
y = 0
for k in range(0, len(x)):
 aux_saques = dados.loc[(dados["TRANSAÇÃO"] == 'SAQUE CASH/ATM BB') & (dados["NOME PORTADOR"] == x[k])]
 if(len(aux_saques) > y):
  y = len(aux_saques)
  z = x[k]

aux = dados.loc[(dados['NOME PORTADOR'] == z)]
saq_total = aux['VALOR TRANSAÇÃO']
org = aux['NOME ÓRGÃO SUPERIOR']

a =[]
for b in org:
 if b not in a:
  a.append(b)

print('O portador: ', z)
print('Pertencente ao órgão: ', a)
print('Gastou um total de RS',round(sum(saq_total), 2))



