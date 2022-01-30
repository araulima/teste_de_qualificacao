# -*- coding: utf-8 -*-

import pandas as pd
dados = pd.read_excel('teste.xlsx')
dados['NOME ÓRGÃO SUPERIOR'] = dados['NOME ÓRGÃO SUPERIOR'].astype(object)

trans_sig = dados.loc[(dados["NOME PORTADOR"] == "Sigiloso")]
orgao = trans_sig['CÓDIGO ÓRGÃO SUPERIOR']

x = []
for i in orgao:
 if i not in x:
  x.append(i)

z= []
y=0
for k in range(0, len(x)):
 trans_sig_orgao_econ = dados.loc[(dados["NOME PORTADOR"] == "Sigiloso") & (dados["CÓDIGO ÓRGÃO SUPERIOR"] == x[k])]
 if(len(trans_sig_orgao_econ) > y):
  y = len(trans_sig_orgao_econ)
  z = trans_sig_orgao_econ

total_gasto = trans_sig_orgao_econ['VALOR TRANSAÇÃO']

a = []
for b in z['NOME ÓRGÃO SUPERIOR']:
 if b not in a:
  a.append(b)

print('Foi o órgão ', a)
print('Um total de RS ', round(sum(total_gasto), 2))


